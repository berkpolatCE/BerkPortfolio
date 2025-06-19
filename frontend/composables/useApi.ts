export const useApi = () => {
  // Use relative path so requests go through the Nuxt server proxy
  const baseURL = '/api/v1'

  const fetchData = async <T>(endpoint: string): Promise<T> => {
    try {
      const response = await $fetch(`${baseURL}${endpoint}`, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      return response.data as T
    } catch (error) {
      console.error(`API Error: ${endpoint}`, error)
      console.error(`Failed URL: ${baseURL}${endpoint}`)
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
    getPhoto: () => fetchData('/photo')
  }
}