// JS: Add interactive behavior for project cards and contact form

// Add alert on project cards click or enter key press for accessibility
document.querySelectorAll('.project-card').forEach(card => {
  // Click event
  card.addEventListener('click', () => {
    alert('You clicked on ' + card.textContent);
  });
  // Keyboard event for enter key on focusable elements
  card.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      alert('You selected ' + card.textContent);
    }
  });
});

