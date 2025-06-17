<template>
  <div>
    <!-- Header -->
    <section class="pt-20 pb-12 bg-secondary/30">
      <div class="container mx-auto px-6">
        <h1 class="font-display text-4xl md:text-5xl font-bold mb-4">All Projects</h1>
        <p class="text-text-secondary text-lg">A comprehensive look at my work</p>
      </div>
    </section>
    
    <!-- Projects grid -->
    <section class="py-16">
      <div class="container mx-auto px-6">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <ProjectCard 
            v-for="project in projects" 
            :key="project.id"
            :project="project"
          />
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

// Fetch all projects
const { data: projectsData } = await useAsyncData('all-projects', () => useApi().getProjects())
const projects = computed(() => projectsData.value?.projects || [])

useHead({
  title: 'All Projects - Portfolio'
})
</script>