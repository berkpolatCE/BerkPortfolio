<template>
  <nav class="fixed top-0 left-0 right-0 z-50 bg-primary/80 backdrop-blur-lg border-b border-border/50 transition-all duration-300" :class="{ 'py-2': scrolled, 'py-4': !scrolled }">
    <div class="container mx-auto px-6">
      <div class="flex items-center justify-between">
        <!-- Logo -->
        <NuxtLink to="/" class="font-display text-xl font-semibold hover:text-accent transition-colors">
          Portfolio
        </NuxtLink>
        
        <!-- Desktop menu -->
        <div class="hidden md:flex items-center gap-8">
          <a 
            v-for="item in navItems" 
            :key="item.href"
            :href="item.href"
            @click="smoothScroll"
            class="text-text-secondary hover:text-text-primary transition-colors"
          >
            {{ item.label }}
          </a>
        </div>
        
        <!-- Mobile menu button -->
        <button 
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="md:hidden w-8 h-8 flex flex-col justify-center items-center gap-1.5"
        >
          <span class="w-6 h-0.5 bg-text-secondary transition-all duration-300" :class="{ 'rotate-45 translate-y-2': mobileMenuOpen }"></span>
          <span class="w-6 h-0.5 bg-text-secondary transition-all duration-300" :class="{ 'opacity-0': mobileMenuOpen }"></span>
          <span class="w-6 h-0.5 bg-text-secondary transition-all duration-300" :class="{ '-rotate-45 -translate-y-2': mobileMenuOpen }"></span>
        </button>
      </div>
    </div>
    
    <!-- Mobile menu -->
    <Transition name="mobile-menu">
      <div v-if="mobileMenuOpen" class="md:hidden absolute top-full left-0 right-0 bg-primary border-b border-border">
        <div class="container mx-auto px-6 py-4">
          <a 
            v-for="item in navItems" 
            :key="item.href"
            :href="item.href"
            @click="closeMobileMenu"
            class="block py-2 text-text-secondary hover:text-text-primary transition-colors"
          >
            {{ item.label }}
          </a>
        </div>
      </div>
    </Transition>
  </nav>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const scrolled = ref(false)
const mobileMenuOpen = ref(false)

const navItems = [
  { label: 'Home', href: '/#' },
  { label: 'Projects', href: '/#projects' },
  { label: 'Skills', href: '/#skills' },
  { label: 'Contact', href: '/#contact' }
]

const handleScroll = () => {
  scrolled.value = window.scrollY > 50
}

const smoothScroll = (e: Event) => {
  e.preventDefault()
  const target = e.target as HTMLAnchorElement
  const href = target.getAttribute('href')
  
  if (href?.startsWith('/#')) {
    const elementId = href.substring(2)
    const element = document.getElementById(elementId)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
  }
}

const closeMobileMenu = (e: Event) => {
  smoothScroll(e)
  mobileMenuOpen.value = false
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  handleScroll()
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: opacity 0.3s, transform 0.3s;
}

.mobile-menu-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.mobile-menu-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>