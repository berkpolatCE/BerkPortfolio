<template>
  <div>
    <!-- Fixed Logo at Top Left -->
    <div class="fixed top-4 left-4 z-50">
      <a 
        href="/" 
        class="block cursor-pointer"
      >
        <img
          ref="logoImg"
          src="/images/SOCRadar-Logo-white.png-1.webp"
          alt="SOCRadar"
          class="h-12 w-auto transition-transform duration-300 hover:scale-105"
          @load="animateLogo"
        />
      </a>
    </div>

    <!-- Menu Toggle Button -->
    <button
      v-if="isHomePage"
      @click="toggleSidebar"
      class="fixed top-4 right-4 z-50 p-3 rounded-lg bg-primary/20 backdrop-blur-sm border border-border/30 hover:bg-primary/30 transition-all duration-300"
      aria-label="Toggle menu"
    >
      <svg
        class="w-6 h-6 text-foreground transition-transform duration-300"
        :class="{ 'rotate-180': isSidebarOpen }"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M4 6h16M4 12h16M4 18h16"
        />
      </svg>
    </button>

    <!-- Vertical Sidebar Navigation -->
    <nav
      v-if="isHomePage"
      ref="sidebar"
      :class="[
        'fixed top-0 right-0 h-full w-72 bg-primary/95 backdrop-blur-xl border-l border-border/50 z-40',
        'transform transition-transform duration-300 ease-out shadow-xl',
        isSidebarOpen ? 'translate-x-0' : 'translate-x-full'
      ]"
      @mouseenter="handleMouseEnter"
      @mouseleave="handleMouseLeave"
    >
      <div class="flex flex-col h-full pt-20 pb-8 px-6">
        <!-- Navigation Items -->
        <ul class="space-y-4" ref="navList">
          <li
            v-for="(item, index) in navItems"
            :key="item.label"
            class="nav-item"
            :data-index="index"
          >
            <NuxtLink
              v-if="item.type === 'page'"
              :to="item.href"
              @click.native="(e) => handleNavClick(e, item)"
              class="group block py-4 px-5 rounded-lg text-text-secondary hover:text-text-primary hover:bg-white/10 transition-all duration-200 font-medium text-lg relative overflow-hidden"
            >
              <span class="relative z-10">{{ item.label }}</span>
              <span class="absolute inset-0 bg-accent/20 transform -translate-x-full group-hover:translate-x-0 transition-transform duration-300"></span>
            </NuxtLink>
            <a
              v-else
              :href="item.href"
              @click="(e) => handleNavClick(e, item)"
              class="group block py-4 px-5 rounded-lg text-text-secondary hover:text-text-primary hover:bg-white/10 transition-all duration-200 font-medium text-lg relative overflow-hidden"
            >
              <span class="relative z-10">{{ item.label }}</span>
              <span class="absolute inset-0 bg-accent/20 transform -translate-x-full group-hover:translate-x-0 transition-transform duration-300"></span>
            </a>
          </li>
        </ul>

        <!-- Social Links Section (Optional) -->
        <div class="mt-auto pt-8 border-t border-border/30">
          <p class="text-sm text-text-secondary mb-4">Connect</p>
          <div class="flex gap-4">
            <a
              v-if="contactData?.github"
              :href="contactData.github"
              target="_blank"
              rel="noopener noreferrer"
              class="text-text-secondary hover:text-text-primary transition-colors"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
              </svg>
            </a>
            <a
              v-if="contactData?.linkedin"
              :href="contactData.linkedin"
              target="_blank"
              rel="noopener noreferrer"
              class="text-text-secondary hover:text-text-primary transition-colors"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </nav>

    <!-- Invisible trigger area for auto-show -->
    <div
      v-if="isHomePage && !isMobile && !isSidebarOpen"
      class="fixed top-0 right-0 w-32 h-full z-30"
      @mouseenter="showSidebar"
      style="background: transparent;"
    ></div>

    <!-- Mobile Menu Overlay -->
    <Transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="isHomePage && isSidebarOpen && isMobile"
        class="fixed inset-0 bg-black/50 backdrop-blur-sm z-30"
        @click="closeSidebar"
      ></div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, nextTick, computed } from 'vue'
import { gsap } from 'gsap'
import { useRoute } from '#app'

const route = useRoute()

// Import scroll utility - delay until after route is initialized
let scrollToElement: ((elementId: string, offset?: number) => void) | undefined

onMounted(() => {
  const scrollUtils = useScrollTo()
  scrollToElement = scrollUtils.scrollToElement
})

const navItems = [
  { label: 'Home', href: '/', type: 'page', forceReload: true },
  { label: 'Projects', href: '/#projects', type: 'section' },
  { label: 'Skills', href: '/#skills', type: 'section' },
  { label: 'Contact', href: '/#contact', type: 'section' }
]

const isSidebarOpen = ref(false)
const isMobile = ref(false)
const autoHideTimer = ref<number | null>(null)
const sidebar = ref<HTMLElement | null>(null)
const navList = ref<HTMLElement | null>(null)
const logoImg = ref<HTMLElement | null>(null)

// Check if we're on the home page
const isHomePage = ref(route.path === '/')

// Fetch contact data
const { data: contactData } = await useAsyncData('contact', () => useApi().getContact())

// Check if mobile
const checkMobile = () => {
  isMobile.value = window.innerWidth < 768
}

// Auto-hide functionality
const startAutoHideTimer = () => {
  if (autoHideTimer.value) {
    clearTimeout(autoHideTimer.value)
  }
  autoHideTimer.value = window.setTimeout(() => {
    if (!isMobile.value) {
      closeSidebar()
    }
  }, 1000) // 500 milisecond timer
}

const handleMouseEnter = () => {
  if (autoHideTimer.value) {
    clearTimeout(autoHideTimer.value)
  }
}

const handleMouseLeave = () => {
  if (!isMobile.value && isSidebarOpen.value) {
    startAutoHideTimer()
  }
}

const handleTriggerLeave = () => {
  // Don't start timer if mouse is still over the sidebar
  if (!isMobile.value && !isSidebarOpen.value) {
    startAutoHideTimer()
  }
}

// Sidebar controls
const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
}

const showSidebar = () => {
  // Clear any existing timer first
  if (autoHideTimer.value) {
    clearTimeout(autoHideTimer.value)
  }
  
  // Open sidebar
  isSidebarOpen.value = true
  
  // Don't start timer immediately - wait for mouse to leave
}

const closeSidebar = () => {
  isSidebarOpen.value = false
  if (autoHideTimer.value) {
    clearTimeout(autoHideTimer.value)
  }
}

// Navigation handling
const handleNavClick = (e: Event, item?: any) => {
  const target = e.currentTarget as HTMLAnchorElement | HTMLElement
  const href = target.getAttribute('href') || target.getAttribute('to')
  
  // Handle home button click
  if (href === '/' && item?.forceReload) {
    e.preventDefault()
    closeSidebar()
    // Force full page reload for home
    setTimeout(() => {
      window.location.href = '/'
    }, 300)
    return
  }
  
  // Handle home button click when already on home page
  if (href === '/' && isHomePage.value && scrollToElement) {
    e.preventDefault()
    scrollToElement('') // Scroll to top
    setTimeout(() => {
      closeSidebar()
    }, 300)
    return
  }
  
  // Handle section scrolling for anchor links when on home page
  if (href && href.startsWith('/#') && isHomePage.value && scrollToElement) {
    e.preventDefault()
    
    if (href === '/#' || href === '/') {
      // Scroll to top for home
      scrollToElement('')
    } else {
      // Extract section id and scroll to it with offset
      const elementId = href.substring(2)
      scrollToElement(elementId, 80) // 80px offset for fixed header
    }
  }
  
  // Close sidebar after navigation
  setTimeout(() => {
    closeSidebar()
  }, 300)
}

// Logo animation
const animateLogo = () => {
  if (logoImg.value) {
    gsap.fromTo(logoImg.value, 
      {
        scale: 0,
        rotation: -180,
        opacity: 0
      },
      {
        scale: 1,
        rotation: 0,
        opacity: 1,
        duration: 0.8,
        ease: 'back.out(1.7)'
      }
    )
  }
}

// Watch sidebar state for animations
watch(isSidebarOpen, async (newVal) => {
  await nextTick()
  
  if (newVal && navList.value) {
    // Set initial state for nav items
    const items = navList.value.querySelectorAll('.nav-item')
    gsap.set(items, {
      opacity: 0,
      x: 30
    })
    
    // Animate nav items when sidebar opens
    gsap.to(items, {
      opacity: 1,
      x: 0,
      duration: 0.4,
      stagger: 0.08,
      ease: 'power2.out'
    })
  }
})

// Watch route changes to manage sidebar visibility
watch(() => route.path, (newPath) => {
  // Update isHomePage reactively
  isHomePage.value = newPath === '/'
  
  // Always close sidebar when route changes
  if (isSidebarOpen.value) {
    closeSidebar()
  }
  
  // Clear any auto-hide timers
  if (autoHideTimer.value) {
    clearTimeout(autoHideTimer.value)
    autoHideTimer.value = null
  }
}, { immediate: true })

// Global click handler to close sidebar when navigating via external links
const handleGlobalClick = (e: MouseEvent) => {
  const target = e.target as HTMLElement
  const link = target.closest('a')
  
  if (link && isSidebarOpen.value && !sidebar.value?.contains(link)) {
    const href = link.getAttribute('href')
    // Close sidebar for any navigation that leaves the current page
    if (href && !href.startsWith('#') && href !== '/') {
      closeSidebar()
    }
  }
}

onMounted(() => {
  checkMobile()
  window.addEventListener('resize', checkMobile)
  
  // Initial logo animation
  animateLogo()
  
  // Ensure sidebar state is correct on mount
  if (!isHomePage.value) {
    isSidebarOpen.value = false
  }
  
  // Add global click handler
  document.addEventListener('click', handleGlobalClick)
})

onUnmounted(() => {
  window.removeEventListener('resize', checkMobile)
  document.removeEventListener('click', handleGlobalClick)
  if (autoHideTimer.value) {
    clearTimeout(autoHideTimer.value)
  }
})
</script>

<style scoped>
/* Custom scrollbar for sidebar */
nav::-webkit-scrollbar {
  width: 4px;
}

nav::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.1);
}

nav::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 2px;
}

nav::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.3);
}
</style>