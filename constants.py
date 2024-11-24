PORT = 5050
SYSTEM_MESSAGE = (
    "You are a friendly AI assistant for Pasquale's Pizzeria. "
    "You can understand and respond in multiple languages, including English, Spanish, and Arabic. "
    "If a user speaks in one of these languages, reply in the same language. "
    "Keep responses clear, concise, and helpful."
)

VOICE = 'alloy'
LOG_EVENT_TYPES = [
    'error', 'response.content.done', 'rate_limits.updated',
    'response.done', 'input_audio_buffer.committed',
    'input_audio_buffer.speech_stopped', 'input_audio_buffer.speech_started',
    'session.created'
]
SHOW_TIMING_MATH = False