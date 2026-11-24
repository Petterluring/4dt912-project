import { useEffect, useRef, useState } from 'react'
import { getHelloMessage } from '../api/HelloFastAPI'

export default function HelloFastAPIComp() {
  const [message, setMessage] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const request = useRef<AbortController | null>(null)

  useEffect(() => () => request.current?.abort(), [])

  async function sendRequest() {
    const controller = new AbortController()
    request.current = controller
    setLoading(true)
    setError('')

    try {
      const result = await getHelloMessage(controller.signal)
      if (!controller.signal.aborted) {
        setMessage(result)
      }
    } catch (err) {
      if (!controller.signal.aborted) {
        setError(err instanceof Error ? err.message : 'Request failed')
      }
    } finally {
      if (request.current === controller) {
        request.current = null
        setLoading(false)
      }
    }
  }

  function clearContent() {
    request.current?.abort()
    request.current = null
    setLoading(false)
    setMessage('')
    setError('')
  }

  return (
    <section className="hello-api">
      <h2>FastAPI message</h2>
      <div className="message-box" aria-live="polite">{message}</div>
      {error && <p className="request-error" role="alert">{error}</p>}
      <div className="hello-actions">
        <button className="send-button" type="button" onClick={sendRequest} disabled={loading}>
          {loading ? 'Sending...' : 'Send request'}
        </button>
        <button className="clear-button" type="button" onClick={clearContent}>Clear</button>
      </div>
    </section>
  )
}