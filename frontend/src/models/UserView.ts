import { backend, type User, type UserCreateData } from '../backend'

export class UserView {
  users: User[] = []
  currentUser: User = { id: '', username: '', email: '' }
  errors: string[] = []
  loading: boolean = false

  async saveUser(model: User): Promise<User> {
    if (model.id) {
      return await backend.updateUser(model.id, model as UserCreateData)
    } else {
      return await backend.createUser(model as UserCreateData)
    }
  }

  createEmptyUser(): User {
    return { id: '', username: '', email: '' }
  }

  parseError(errorObj: any): string[] {
    const errors: string[] = []

    if (errorObj?.response?.data?.errors) {
      for (const [field, message] of Object.entries(
        errorObj.response.data.errors,
      )) {
        errors.push(`${field}: ${message}`)
      }
    } else if (errorObj?.message) {
      errors.push(errorObj.message)
    } else {
      errors.push('An unexpected error occurred')
    }

    return errors
  }

  validateUser(user: UserCreateData): string[] {
    const errors: string[] = []

    if (!user.username?.trim()) {
      errors.push('Username is required')
    }

    if (!user.email?.trim()) {
      errors.push('Email is required')
    } else if (!this.isValidEmail(user.email)) {
      errors.push('Please enter a valid email address')
    }

    return errors
  }

  private isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return emailRegex.test(email)
  }

  async refreshUsers(): Promise<void> {
    this.loading = true
    const result = await this.handleAsyncOperation(async () => {
      const response = await backend.getUsers()
      return response.data
    })

    if (result.success) {
      this.users = result.data || []
      this.errors = []
    } else {
      this.errors = result.errors
    }
    this.loading = false
  }

  async saveCurrentUser(): Promise<void> {
    const result = await this.handleSaveUser(this.currentUser)

    if (result.success) {
      this.currentUser = this.createEmptyUser()
      this.errors = []
      await this.refreshUsers()
    } else {
      this.errors = result.errors
    }
  }

  async deleteUserById(id: string): Promise<void> {
    const user = this.users.find((u) => u.id === id)

    if (this.confirmDelete(user?.username)) {
      const result = await this.handleDeleteUser(id, this.currentUser)

      if (result.success) {
        if (result.shouldClearForm) {
          this.currentUser = this.createEmptyUser()
        }
        this.errors = []
        await this.refreshUsers()
      } else {
        this.errors = result.errors
      }
    }
  }

  setCurrentUser(user: User): void {
    this.currentUser = { ...user }
  }

  getFormTitle(): string {
    return this.currentUser.id
      ? `Edit User ID#${this.currentUser.id}`
      : 'New User'
  }

  confirmDelete(username?: string): boolean {
    const message = username
      ? `Are you sure you want to delete user "${username}"?`
      : 'Are you sure you want to delete this user?'
    return confirm(message)
  }

  async handleAsyncOperation<T>(
    operation: () => Promise<T>,
  ): Promise<{ success: boolean; data?: T; errors: string[] }> {
    try {
      const data = await operation()
      return { success: true, data, errors: [] }
    } catch (err) {
      return { success: false, errors: this.parseError(err) }
    }
  }

  async handleSaveUser(
    user: User,
  ): Promise<{ success: boolean; errors: string[] }> {
    // Client-side validation first
    const validationErrors = this.validateUser(user as UserCreateData)
    if (validationErrors.length > 0) {
      return { success: false, errors: validationErrors }
    }

    return await this.handleAsyncOperation(() => this.saveUser(user))
  }

  async handleDeleteUser(
    userId: string,
    currentEditingUser?: User,
  ): Promise<{
    success: boolean
    errors: string[]
    shouldClearForm: boolean
  }> {
    const result = await this.handleAsyncOperation(() =>
      backend.deleteUser(userId),
    )
    const shouldClearForm = currentEditingUser?.id === userId

    return {
      success: result.success,
      errors: result.errors,
      shouldClearForm,
    }
  }
}
