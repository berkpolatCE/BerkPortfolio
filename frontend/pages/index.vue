<template>
  <div>
    <!-- Hero Section -->
    <HeroSection :data="homeData" :loading="pending" />
    
    <!-- About Section -->
    <section class="py-16 bg-white dark:bg-dark-bg">
      <div class="max-container section-padding">
        <AboutSection :data="homeData" :loading="pending" />
      </div>
    </section>
    
    <!-- Projects Section -->
    <section class="py-16 bg-gray-50 dark:bg-dark-card">
      <div class="max-container section-padding">
        <SectionTitle 
          title="Featured Projects"
          subtitle="A selection of my recent work"
          class="mb-12"
        />
        <ProjectGrid :projects="featuredProjects" :loading="projectsPending" />
        
        <div class="text-center mt-12">
          <NuxtLink
            to="/projects"
            class="inline-flex items-center space-x-2 px-6 py-3 bg-primary-600 hover:bg-primary-700 text-white rounded-lg transition-colors duration-200 hover-lift"
          >
            <span>View All Projects</span>
            <Icon name="heroicons:arrow-right" class="w-5 h-5" />
          </NuxtLink>
        </div>
      </div>
    </section>
    
    <!-- Skills Section -->
    <section class="py-16 bg-white dark:bg-dark-bg">
      <div class="max-container section-padding">
        <SectionTitle 
          title="Skills & Expertise"
          subtitle="Technologies and tools I work with"
          class="mb-12"
        />
        <SkillSection :skills="skillsData" :loading="skillsPending" />
      </div>
    </section>
    
    <!-- Contact Section -->
    <section class="py-16 bg-gray-50 dark:bg-dark-card">
      <div class="max-container section-padding">
        <SectionTitle 
          title="Get In Touch"
          subtitle="Let's work together on your next project"
          class="mb-12"
        />
        <ContactSection :contact="contactData" :loading="contactPending" />
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
const api = useApi()

// Fetch all data
const { data: homeData, pending } = await useAsyncData('home', () => api.getHome())
const { data: featuredProjects, pending: projectsPending } = await useAsyncData('featured-projects', () => api.getProjects(true))
const { data: skillsData, pending: skillsPending } = await useAsyncData('skills', () => api.getSkills())
const { data: contactData, pending: contactPending } = await useAsyncData('contact', () => api.getContact())

// Page metadata
useHead({
  title: 'Home'
})
</script>