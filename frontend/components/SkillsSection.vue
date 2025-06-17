<template>
  <section id="skills" class="py-20 md:py-32 bg-secondary/30">
    <div class="container mx-auto px-6">
      <!-- Section header -->
      <div class="text-center mb-16">
        <h2 class="section-title">
          Skills & Expertise
        </h2>
        <p class="text-text-secondary text-lg max-w-2xl mx-auto">
          Technologies and tools I work with
        </p>
      </div>
      
      <!-- Skills tabs -->
      <div class="flex justify-center mb-12">
        <div class="inline-flex bg-primary rounded-lg p-1">
          <button 
            v-for="tab in ['technical', 'soft']" 
            :key="tab"
            @click="activeTab = tab"
            :class="[
              'px-6 py-2 rounded-md font-medium transition-all duration-300',
              activeTab === tab 
                ? 'bg-accent text-primary' 
                : 'text-text-secondary hover:text-text-primary'
            ]"
          >
            {{ tab.charAt(0).toUpperCase() + tab.slice(1) }} Skills
          </button>
        </div>
      </div>
      
      <!-- Skills grid -->
      <div class="skills-container">
        <TransitionGroup 
          name="skill" 
          tag="div" 
          class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4"
        >
          <SkillCard 
            v-for="skill in filteredSkills" 
            :key="skill.name"
            :skill="skill"
            class="skill-item"
          />
        </TransitionGroup>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const activeTab = ref('technical')

// Fetch skills data
const { data: skillsData } = await useAsyncData('skills', () => useApi().getSkills())

const filteredSkills = computed(() => {
  if (!skillsData.value) return []
  
  if (activeTab.value === 'technical') {
    // Flatten all technical skills into a single array
    const technical = skillsData.value.technical
    const allSkills = []
    
    if (technical?.languages) allSkills.push(...technical.languages.map(s => ({ ...s, category: 'Languages' })))
    if (technical?.frontend) allSkills.push(...technical.frontend.map(s => ({ ...s, category: 'Frontend' })))
    if (technical?.backend) allSkills.push(...technical.backend.map(s => ({ ...s, category: 'Backend' })))
    if (technical?.databases) allSkills.push(...technical.databases.map(s => ({ ...s, category: 'Databases' })))
    if (technical?.tools) allSkills.push(...technical.tools.map(s => ({ ...s, category: 'Tools' })))
    
    return allSkills
  } else {
    // Convert soft skills array to objects with name and proficiency
    return skillsData.value.soft?.map(skill => ({
      name: skill,
      level: '90%', // Default level for soft skills
      category: 'Soft Skill'
    })) || []
  }
})

onMounted(() => {
  // Animate section elements
  gsap.from('.section-title', {
    scrollTrigger: {
      trigger: '#skills .section-title',
      start: 'top 80%'
    },
    y: 30,
    opacity: 0,
    duration: 1
  })
})
</script>

<style scoped>
.section-title {
  @apply font-display text-4xl md:text-5xl font-bold mb-4;
  background: linear-gradient(to right, #ffffff 0%, #a3a3a3 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.skill-move,
.skill-enter-active,
.skill-leave-active {
  transition: all 0.5s ease;
}

.skill-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

.skill-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.skill-leave-active {
  position: absolute;
}
</style>