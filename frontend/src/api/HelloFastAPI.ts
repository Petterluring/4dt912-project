export async function getHelloMessage(signal?: AbortSignal): Promise<string> {
  const response = await fetch('/api/hello/', { signal })

  if (!response.ok) {
    throw new Error(`Request failed (${response.status})`)
  }

  const data: unknown = await response.json()
  if (
    typeof data !== 'object' ||
    data === null ||
    !('message' in data) ||
    typeof data.message !== 'string'
  ) {
    throw new Error('Invalid response from the server')
  }

  return data.message
}