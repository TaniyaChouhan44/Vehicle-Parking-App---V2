<template>
  <div class="card mb-3">
    <div class="card-body">
      <h5 class="card-title">{{ lot.prime_location_name }}</h5>
      <p class="card-text">
        Price: ₹{{ lot.price }} <br />
        Address: {{ lot.address }} <br />
        PIN: {{ lot.pin_code }} <br />
        Spots: {{ lot.number_of_spots }}
      </p>
      <button class="btn btn-primary" @click="$emit('view-spots', lot.id)">View Spots</button>
    </div>
  </div>
</template>

<script setup>
defineProps(['lot'])
defineEmits(['view-spots'])
</script>
