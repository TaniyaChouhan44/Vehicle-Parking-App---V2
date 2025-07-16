<template>
  <div class="card mb-3">
    <div class="card-body">
      <h5 class="card-title">Reservation #{{ res.id }}</h5>
      <p class="card-text">
        Lot: {{ res.lot_name }} <br />
        Spot: {{ res.spot_number }} <br />
        From: {{ formatDate(res.parking_timestamp) }} <br />
        To: {{ res.leaving_timestamp ? formatDate(res.leaving_timestamp) : 'Active' }} <br />
        Cost: ₹{{ res.parking_cost || 'Pending' }}
      </p>
      <button class="btn btn-danger" v-if="!res.leaving_timestamp" @click="$emit('leave', res.id)">Leave Spot</button>
    </div>
  </div>
</template>

<script setup>
import { format } from 'date-fns'

const props = defineProps(['res'])
defineEmits(['leave'])

function formatDate(dt) {
  return format(new Date(dt), 'dd MMM yyyy, hh:mm a')
}
</script>
