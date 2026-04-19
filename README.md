

✅ 1. FIX TOPBAR (IMPORTANT)
👉 Add this to your CSS:
CSS
.topbar {
  display: flex;
  align-items: center;
  gap: 15px;
  background: white;
  padding: 12px 20px;
  border-radius: 10px;
  margin-bottom: 20px;
}
✅ 2. MAKE MENU BUTTON VISIBLE
👉 Add this (VERY IMPORTANT):
CSS
#menuToggle {
  font-size: 24px;
  background: #2563eb;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 8px;
  cursor: pointer;

  /* force visibility */
  z-index: 1000;
  position: relative;
}

#menuToggle:hover {
  background: #1e40af;
}
✅ 3. FIX SIDEBAR POSITION
👉 Add:
CSS
.sidebar {
  position: fixed;
  left: 0;
  top: 0;
  height: 100%;
}
✅ 4. FIX MAIN ALIGNMENT
👉 Replace your .main CSS with:
CSS
.main {
  margin-left: 220px;
  width: 100%;
  padding: 20px;
  transition: 0.3s;
}

.main.expanded {
  margin-left: 70px;
}
✅ 5. ENSURE BUTTON EXISTS IN HTML
👉 Your header MUST look like this:
HTML
<header class="topbar">
  <button id="menuToggle">☰</button>
  <h2>Insights</h2>
</header>
