<template>
  <div class="container mt-5">
    <h2 class="text-center mb-4">All Parking Spots</h2>
    
    <table v-if="spots.length" class="table table-bordered table-striped">
      <thead class="table-dark">
        <tr>
          <th>ID</th>
          <th>Lot ID</th>
          <th>Spot Number</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="spot in spots" :key="spot.id">
          <td>{{ spot.id }}</td>
          <td>{{ spot.lot_id }}</td>
          <td>{{ spot.spot_number }}</td>
          <td>{{ spot.status }}</td>
          <td>
            <button class="btn btn-danger btn-sm" @click="deleteSpot(spot.id)">
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-else class="alert alert-info text-center">
      No parking spots found.
    </div>

    <div v-if="error" class="alert alert-danger mt-3 text-center">
      {{ error }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const spots = ref([])
const error = ref('')

onMounted(async () => {
  try {
    const token = localStorage.getItem('token')
    const res = await fetch(import.meta.env.VITE_BASEURL + 'admin/parking_spots', {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
      }
    })

    const data = await res.json()

    if (!res.ok) {
      error.value = data.msg || 'Failed to load parking spots'
      return
    }

    spots.value = data
  } catch (err) {
    console.error(err)
    error.value = 'Server error. Please try again later.'
  }
})


const deleteSpot = async (id) => {
  if (!confirm('Are you sure you want to delete this parking spot?')) return

  try {
    const token = localStorage.getItem('token')
    const res = await fetch(
      `${import.meta.env.VITE_BASEURL}admin/parking_spots/${id}`,
      {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + token
        }
      }
    )

    const data = await res.json()

    if (!res.ok) {
      error.value = data.message || 'Failed to delete parking spot'
      return
    }


    spots.value = spots.value.filter(spot => spot.id !== id)
  } catch (err) {
    console.error(err)
    error.value = 'Server error. Please try again later.'
  }
}
</script>