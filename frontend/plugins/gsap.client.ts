import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

export default defineNuxtPlugin(() => {
  if (process.client) {
    gsap.registerPlugin(ScrollTrigger)
    
    // Configure ScrollTrigger
    ScrollTrigger.config({
      limitCallbacks: true,
      ignoreMobileResize: true
    })
    
    // Refresh ScrollTrigger on route change
    const router = useRouter()
    router.afterEach(() => {
      setTimeout(() => {
        ScrollTrigger.refresh()
      }, 100)
    })
  }
})