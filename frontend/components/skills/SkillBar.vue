<template>
  <div class="space-y-2">
    <div class="flex justify-between items-center">
      <span class="font-medium text-gray-700 dark:text-gray-300">
        {{ skill.name }}
      </span>
      <span class="text-sm text-gray-500 dark:text-gray-400">
        {{ skill.level }}
      </span>
    </div>
    
    <div class="h-3 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
      <div
        ref="progressBar"
        class="skill-bar-fill"
        :style="{ width: isVisible ? skill.level : '0%' }"
      ></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useIntersectionObserver } from '@vueuse/core'
import type { SkillCategory } from '~/composables/useApi'

interface Props {
  skill: SkillCategory
}

const props = defineProps<Props>()

const progressBar = ref<HTMLElement>()
const isVisible = ref(false)

useIntersectionObserver(
  progressBar,
  ([{ isIntersecting }]) => {
    if (isIntersecting && !isVisible.value) {
      isVisible.value = true
    }
  },
  { threshold: 0.1 }
)
</script>