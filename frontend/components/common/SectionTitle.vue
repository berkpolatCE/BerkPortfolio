<template>
  <div class="text-center animate-fade-up">
    <h2 class="text-4xl font-display font-bold gradient-text mb-4">
      {{ title }}
    </h2>
    <p v-if="subtitle" class="text-xl text-gray-600 dark:text-gray-400">
      {{ subtitle }}
    </p>
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string
  subtitle?: string
}

defineProps<Props>()
</script>