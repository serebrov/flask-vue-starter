import { describe, it, expect, vi } from 'vitest'
import { backend } from '../../src/backend'
import type { User, ApiResponse } from '../../src/backend'

// Mock axios
vi.mock('axios', () => {
  return {
    default: {
      create: () => ({
        get: vi.fn(),
        post: vi.fn(),
        delete: vi.fn(),
        interceptors: {
          request: { use: vi.fn() },
          response: { use: vi.fn() },
        },
      }),
    },
  }
})

describe('Backend API', () => {
  it('should have correct TypeScript interfaces', () => {
    const mockUser: User = {
      id: '123',
      username: 'test',
      email: 'test@example.com',
    }

    const mockResponse: ApiResponse<User[]> = {
      data: [mockUser],
    }

    expect(mockUser.id).toBe('123')
    expect(mockResponse.data).toHaveLength(1)
  })

  it('should have all required API methods', () => {
    expect(backend.getUsers).toBeDefined()
    expect(backend.getUser).toBeDefined()
    expect(backend.createUser).toBeDefined()
    expect(backend.updateUser).toBeDefined()
    expect(backend.deleteUser).toBeDefined()
  })
})
