<template>
  <div>
    <NuxtRouteAnnouncer />
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
// Set up page metadata
useHead({
  titleTemplate: (titleChunk) => {
    return titleChunk ? `${titleChunk} - Portfolio` : 'Portfolio'
  }
})
</script>
