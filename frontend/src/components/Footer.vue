<template>
  <footer class="bg-dark text-white text-center py-3 mt-5">
    <div class="container">
      <p class="mb-0">&copy; {{ year }} Vehicle Parking App. All rights reserved.</p>
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear()
</script>

<style scoped>
footer {
  position: relative;
  bottom: 0;
  width: 100%;
}
</style>
