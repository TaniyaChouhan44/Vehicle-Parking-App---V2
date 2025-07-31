from flask import current_app
import csv
import io
import smtplib
from celery_app import celery
from models import Reservation
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from app import create_app
from extensions import db

@celery.task(name="tasks.csv_tasks.export_csv_task")
def export_csv_task():
    print("Task started: export_csv_task")

    app = create_app()
    with app.app_context():
        db.create_all()  # ensure tables exist

        # Check if any reservations exist
        reservations = Reservation.query.all()
        if not reservations:
            print("No reservations found.")
            return

        # Generate CSV
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Username", "Email", "Spot", "Lot", "Start Time", "End Time", "Cost"])

        for r in reservations:
            if r.user and r.spot and r.spot.lot:
                writer.writerow([
                    r.user.username,
                    r.user.email,
                    r.spot.spot_number,
                    r.spot.lot.prime_location_name,
                    r.parking_timestamp.strftime("%Y-%m-%d %H:%M:%S") if r.parking_timestamp else "N/A",
                    r.leaving_timestamp.strftime("%Y-%m-%d %H:%M:%S") if r.leaving_timestamp else "Ongoing",
                    r.parking_cost if r.parking_cost else 0.0
                ])
            else:
                print(f"Skipping reservation ID {r.id} due to missing relationships.")

        csv_data = output.getvalue()

        # Optional: Save locally for testing
        with open("test_export.csv", "w", encoding="utf-8") as f:
            f.write(csv_data)

       
        sender_email = current_app.config.get("MAIL_USERNAME")
        password = current_app.config.get("MAIL_PASSWORD")
        receiver_email = sender_email 

        if not sender_email or not password:
            print("Error: MAIL_USERNAME or MAIL_PASSWORD not configured.")
            return

        # Prepare email
        msg = MIMEMultipart()
        msg["Subject"] = "Vehicle Parking App - CSV Export"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        msg.attach(MIMEText("Please find attached the latest CSV export of reservations.", "plain"))

        attachment = MIMEApplication(csv_data.encode("utf-8"), _subtype="csv")
        attachment.add_header("Content-Disposition", "attachment", filename="reservation_export.csv")
        msg.attach(attachment)

        # Send email
        try:
            print("Connecting to SMTP server...")
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            print("CSV report emailed successfully")
        except Exception as e:
            print(f"Error sending email: {e}")


