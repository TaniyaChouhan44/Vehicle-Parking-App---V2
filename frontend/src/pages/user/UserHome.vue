<template>
  <div class="container mt-4">
    <h2 class="text-center mb-4">Welcome to User Dashboard</h2>

    <!-- Use the component -->
    <AvailableParkingLots />

    <router-link to="/user/available-lots" class="btn btn-outline-primary w-100 my-2">
      View Available Parking Lots
    </router-link>
  </div>
</template>

