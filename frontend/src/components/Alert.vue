<template>
  <div v-if="msg" :class="`alert alert-${type}`" role="alert">
    {{ msg }}
  </div>
</template>

<script setup>
defineProps({
  msg: String,
  type: {
    type: String,
    default: 'success' // or 'danger', 'warning'
  }
})
</script>
