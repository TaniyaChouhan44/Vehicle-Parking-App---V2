<template>
  <div class="card mb-2">
    <div class="card-body d-flex justify-content-between align-items-center">
      <div>
        <strong>Spot #{{ spot.spot_number }}</strong> - 
        <span :class="statusClass">{{ spot.status === 'A' ? 'Available' : 'Occupied' }}</span>
      </div>
      <button 
        class="btn btn-success"
        :disabled="spot.status !== 'A'"
        @click="$emit('book', spot.id)">
        Book
      </button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps(['spot'])

const statusClass = computed(() => {
  return props.spot.status === 'A' ? 'text-success' : 'text-danger'
})

defineEmits(['book'])
</script>
