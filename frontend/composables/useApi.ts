export const useApi = () => {
  const config = useRuntimeConfig()
  const baseURL = config.public.apiBase

  const fetchData = async <T>(endpoint: string): Promise<T> => {
    try {
      console.log(`[API] Fetching: ${baseURL}${endpoint}`)
      
      const response = await $fetch(`${baseURL}${endpoint}`, {
        headers: {
          'Content-Type': 'application/json'
        },
        // Add retry logic
        retry: 2,
        retryDelay: 1000,
        // Set timeout
        timeout: 10000
      })
      
      // Validate response structure
      if (!response || typeof response !== 'object') {
        throw new Error('Invalid response format')
      }
      
      console.log(`[API] Success: ${endpoint}`, response)
      return response.data as T
    } catch (error) {
      console.error(`[API] Error fetching ${endpoint}:`, error)
      
      // Provide more context in error messages
      if (error instanceof Error) {
        if (error.message.includes('fetch')) {
          throw new Error(`Network error: Unable to connect to API at ${baseURL}`)
        }
      }
      
      throw error
    }
  }

  return {
    getHome: () => fetchData('/home'),
    getProjects: (featured?: boolean) => 
      fetchData(`/projects${featured ? '?featured=true' : ''}`),
    getProject: (id: string) => fetchData(`/projects/${id}`),
    getSkills: () => fetchData('/skills'),
    getSkillsByCategory: (category: string) => fetchData(`/skills/${category}`),
    getContact: () => fetchData('/contact'),
    getCv: () => fetchData('/cv')
  }
}