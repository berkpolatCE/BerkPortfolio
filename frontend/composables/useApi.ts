export const useApi = () => {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase

  const fetchData = async <T>(endpoint: string): Promise<T> => {
    try {
      const response = await $fetch(`${apiBase}${endpoint}`)
      
      // Check if response has success property and data
      if (response && typeof response === 'object' && 'success' in response) {
        if (response.success && 'data' in response) {
          return response.data as T
        } else if (!response.success && 'error' in response) {
          throw new Error(response.error as string)
        }
      }
      
      // If response doesn't follow expected format, return as is
      return response as T
    } catch (error) {
      console.error(`API Error for ${endpoint}:`, error)
      throw error
    }
  }

  return {
    getHome: () => fetchData<HomeData>('/home'),
    getProjects: async (featured?: boolean) => {
      const data = await fetchData<ProjectsResponse>('/projects' + (featured ? '?featured=true' : ''))
      return data.projects || data
    },
    getProject: (id: number) => fetchData<Project>(`/projects/${id}`),
    getSkills: () => fetchData<SkillsData>('/skills'),
    getPhoto: () => fetchData<PhotoData>('/photo'),
    getContact: () => fetchData<ContactData>('/contact'),
    getCv: () => fetchData<CvData>('/cv'),
  }
}

// Type definitions
export interface HomeData {
  name: string
  title: string
  about: string
  image_url: string
  location: string
  languages: string[]
  interests: string[]
}

export interface Project {
  id: number
  title: string
  description: string
  technologies: string[]
  github_url: string
  live_url: string | null
  image: string
  featured: boolean
}

export interface ProjectsResponse {
  projects: Project[]
  count: number
}

export interface SkillCategory {
  name: string
  level: string
}

export interface SkillsData {
  technical: {
    languages: SkillCategory[]
    frontend: SkillCategory[]
    backend: SkillCategory[]
    databases: SkillCategory[]
    tools: SkillCategory[]
  }
  soft: string[]
}

export interface PhotoData {
  profile_photo: string
  gallery: Array<{
    id: number
    url: string
    caption: string
    date: string
  }>
}

export interface ContactData {
  email: string
  phone: string
  linkedin: string
  github: string
  twitter: string
  instagram: string
  availability: string
}

export interface CvData {
  filename: string
  url: string
  last_updated: string
}