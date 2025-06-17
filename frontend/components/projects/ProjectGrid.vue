<template>
  <div>
    <div v-if="loading" class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
      <div v-for="i in 3" :key="i" class="skeleton aspect-[4/3] rounded-xl"></div>
    </div>
    
    <div v-else-if="projects?.length" class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
      <ProjectCard
        v-for="(project, index) in projects"
        :key="project.id"
        :project="project"
        :style="{ animationDelay: `${index * 100}ms` }"
        class="animate-fade-up"
      />
    </div>
    
    <div v-else class="text-center py-12">
      <p class="text-gray-500 dark:text-gray-400">No projects found.</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Project } from '~/composables/useApi'

interface Props {
  projects?: Project[]
  loading?: boolean
}

defineProps<Props>()
</script>