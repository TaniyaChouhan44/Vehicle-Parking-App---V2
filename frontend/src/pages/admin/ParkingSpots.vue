<script setup>
import { ref, onMounted } from 'vue'

const parkingSpots = ref([])
const newSpot = ref({
  slot_number: '',
  is_available: true
})
const error = ref('')
const success = ref('')

// Fetch existing spots on load
async function fetchSpots() {
  try {
    const res = await fetch(import.meta.env.VITE_BASEURL + 'admin/slots', {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('token')
      }
    })
    const data = await res.json()
    parkingSpots.value = data
  } catch (err) {
    console.error(err)
    error.value = 'Error fetching parking spots'
  }
}

// Add a new spot
async function addSpot() {
  error.value = ''
  success.value = ''
  if (!newSpot.value.slot_number) {
    error.value = 'Slot number is required'
    return
  }

  try {
    const res = await fetch(import.meta.env.VITE_BASEURL + 'admin/slots', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('token')
      },
      body: JSON.stringify(newSpot.value)
    })

    const data = await res.json()
    if (res.ok) {
      success.value = 'Slot added successfully'
      newSpot.value.slot_number = ''
      newSpot.value.is_available = true
      fetchSpots()
    } else {
      error.value = data.msg || 'Failed to add slot'
    }
  } catch (err) {
    console.error(err)
    error.value = 'Server error'
  }
}

onMounted(fetchSpots)
</script>

<template>
  <div class="container mt-4">
    <h2 class="mb-4 text-center">Manage Parking Spots</h2>

    <div class="mb-4">
      <h5>Add New Spot</h5>
      <div class="row g-2">
        <div class="col-md-4">
          <input type="text" class="form-control" placeholder="Slot Number" v-model="newSpot.slot_number" />
        </div>
        <div class="col-md-4">
          <select class="form-select" v-model="newSpot.is_available">
            <option :value="true">Available</option>
            <option :value="false">Not Available</option>
          </select>
        </div>
        <div class="col-md-4">
          <button class="btn btn-primary w-100" @click="addSpot">Add Spot</button>
        </div>
      </div>
      <div v-if="error" class="text-danger mt-2">{{ error }}</div>
      <div v-if="success" class="text-success mt-2">{{ success }}</div>
    </div>

    <div>
      <h5>All Spots</h5>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Slot ID</th>
            <th>Slot Number</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="spot in parkingSpots" :key="spot.id">
            <td>{{ spot.id }}</td>
            <td>{{ spot.slot_number }}</td>
            <td>
              <span :class="spot.is_available ? 'text-success' : 'text-danger'">
                {{ spot.is_available ? 'Available' : 'Not Available' }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

