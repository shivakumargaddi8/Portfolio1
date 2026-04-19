

/* ===== FIX SIDEBAR OVERLAP (FINAL OVERRIDE) ===== */

.sidebar {
  position: fixed !important;
  left: 0;
  top: 0;
  height: 100%;
  width: 220px;
  z-index: 1000;
}

.main {
  margin-left: 220px !important;
  width: calc(100% - 220px);
  transition: 0.3s;
}

.sidebar.collapsed {
  width: 70px !important;
}

.main.expanded {
  margin-left: 70px !important;
  width: calc(100% - 70px);
}

/* keep flex layout (IMPORTANT — don't change this) */
.layout {
  display: flex !important;
}
