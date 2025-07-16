<template>
  <div class="container mt-4">
    <h2 class="text-center mb-4">Available Parking Lots</h2>
    <div v-if="lots.length === 0" class="text-center">No parking lots available.</div>
    <div v-else class="row">
      <div class="col-md-6 mb-3" v-for="lot in lots" :key="lot.id">
        <div class="card shadow-sm">
          <div class="card-body">
            <h5 class="card-title">{{ lot.name }}</h5>
            <p class="card-text"><strong>Address:</strong> {{ lot.address }}</p>
            <p class="card-text"><strong>Pincode:</strong> {{ lot.pin_code }}</p>
            <p class="card-text"><strong>Price:</strong> ₹{{ lot.price }}</p>
            <p class="card-text"><strong>Total Spots:</strong> {{ lot.total_spots }}</p>
          </div>
        </div>
      </div>
    </div>
    <div v-if="error" class="alert alert-danger text-center">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const lots = ref([])
const error = ref('')

onMounted(async () => {
  try {
    const token = localStorage.getItem('token')
    const res = await fetch(import.meta.env.VITE_BASEURL + 'user/available-lots', {
      headers: { 'Authorization': 'Bearer ' + token }
    })
    const data = await res.json()
    if (res.ok) {
      lots.value = data
    } else {
      error.value = data.msg || "Failed to load parking lots."
    }
  } catch (err) {
    error.value = "Server error. Please try again later."
    console.error(err)
  }
})
</script>
