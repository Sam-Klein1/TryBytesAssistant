PORT = 5050
SYSTEM_MESSAGE = (
    "You are a friendly AI assistant for Pasquale's Pizzeria. "
    "Greet customers warmly and answer their questions about the menu, location, and hours concisely but completely. "
    "Focus on delivering short, clear, and complete responses."
)

VOICE = 'alloy'
LOG_EVENT_TYPES = [
    'error', 'response.content.done', 'rate_limits.updated',
    'response.done', 'input_audio_buffer.committed',
    'input_audio_buffer.speech_stopped', 'input_audio_buffer.speech_started',
    'session.created'
]
SHOW_TIMING_MATH = False