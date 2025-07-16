<template>
  <div class="container py-5">
    <div class="text-center mb-4">
      <h1 class="display-5 fw-bold">🚗 Vehicle Parking App</h1>
      <p class="lead">
        Book your 4-wheeler parking spot in just a few clicks.
      </p>
    </div>

    <div class="d-flex flex-column flex-md-row justify-content-center gap-3">
      <router-link to="/login" class="btn btn-primary btn-lg w-100 w-md-auto">
        Login
      </router-link>

      <router-link to="/register" class="btn btn-outline-primary btn-lg w-100 w-md-auto">
        Register
      </router-link>
    </div>

    <div class="mt-5 text-center text-muted">
      <p>Developed for parking lots with real-time tracking and role-based dashboards.</p>
    </div>
    
  </div>
</template>

<script setup>
// No logic needed here
</script>

<style scoped>
.container {
  min-height: 90vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
