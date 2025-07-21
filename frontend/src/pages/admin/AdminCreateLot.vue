<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mb-4">Create Parking Lot</h2>

    <!-- Create Form -->
    <form @submit.prevent="create_parking_lot" class="mb-6">
      <div class="mb-3">
        <label>Name:</label>
        <input v-model="new_ParkingLot.name" required class="border p-1 w-full" />
      </div>
      <div class="mb-3">
        <label>Price:</label>
        <input v-model.number="new_ParkingLot.price" type="number" required class="border p-1 w-full" />
      </div>
      <div class="mb-3">
        <label>Address:</label>
        <input v-model="new_ParkingLot.address" required class="border p-1 w-full" />
      </div>
      <div class="mb-3">
        <label>Pincode:</label>
        <input v-model="new_ParkingLot.pin_code" required class="border p-1 w-full" />
      </div>
      <div class="mb-3">
        <label>Number of Spots:</label>
        <input v-model.number="new_ParkingLot.number_of_spots" type="number" required class="border p-1 w-full" />
      </div>
      <button class="bg-blue-500 text-white px-4 py-2 rounded" type="submit">Create Lot</button>
    </form>

    <!-- Parking Lots List -->
    <div v-if="parkingLots.length">
      <h2 class="text-xl font-bold mb-4">Existing Parking Lots</h2>
      <table class="table-auto w-full border">
        <thead class="bg-gray-100">
          <tr>
            <th class="border px-4 py-2">ID</th>
            <th class="border px-4 py-2">Name</th>
            <th class="border px-4 py-2">Price</th>
            <th class="border px-4 py-2">Address</th>
            <th class="border px-4 py-2">Pincode</th>
            <th class="border px-4 py-2">Spots</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="lot in parkingLots" :key="lot.id">
            <td class="border px-4 py-2">{{ lot.id }}</td>
            <td class="border px-4 py-2">{{ lot.name }}</td>
            <td class="border px-4 py-2">{{ lot.price }}</td>
            <td class="border px-4 py-2">{{ lot.address }}</td>
            <td class="border px-4 py-2">{{ lot.pin_code }}</td>
            <td class="border px-4 py-2">{{ lot.number_of_spots }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-else class="text-gray-500 mt-4">No parking lots found.</div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'AdminCreateLot',
  setup() {
    const new_ParkingLot = ref({
      name: '',
      price: '',
      address: '',
      pin_code: '',
      number_of_spots: 0
    });

    const parkingLots = ref([]);

    // Load all lots from backend
    const loadLots = async () => {
      try {
        const res = await fetch(import.meta.env.VITE_BASEURL + '/admin/parking_lots');
        const data = await res.json();
        if (res.ok) {
          parkingLots.value = data;
        } else {
          console.error('Failed to load lots:', data.msg);
        }
      } catch (err) {
        console.error('Error loading lots:', err);
      }
    };

    // Create new lot
    const create_parking_lot = async () => {
      try {
        const res = await fetch(import.meta.env.VITE_BASEURL + '/admin/parking_lots', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(new_ParkingLot.value),
        });

        const data = await res.json();

        if (res.ok) {
          alert('Lot created successfully');
          new_ParkingLot.value = {
            name: '',
            price: '',
            address: '',
            pin_code: '',
            number_of_spots: 0
          };
          await loadLots(); // Refresh list
        } else {
          alert(data.msg || 'Failed to create lot');
        }
      } catch (error) {
        console.error('Error creating lot:', error);
      }
    };

    onMounted(loadLots);

    return {
      new_ParkingLot,
      create_parking_lot,
      parkingLots
    };
  }
}
</script>

<style scoped>
input {
  border-radius: 0.25rem;
}
</style>
