# HDIMS — Redesigned UI

A complete premium-SaaS visual redesign of the Health Data Information Management System, covering every page described in the brief: landing, patient/doctor/admin auth (with OTP), patient dashboard + family + records + upload + doctors + appointments + shared access (request → approve → OTP → active/expired) + prescriptions + AI health + notifications + settings, and the parallel doctor and admin sections.

## What this is
This is a **static front-end** (plain HTML/CSS/JS, no build step) implementing the new design system end-to-end. No original project files were provided alongside the brief, so this was built as a fresh, fully-clickable implementation of every screen the brief describes, with realistic sample data.

## Running it
Just open `index.html` in a browser, or serve the folder with any static server:
```
npx serve .
```

## Reconnecting your real backend
Every page currently reads sample data from `assets/js/app.js` (`HDIMS.db.get()`), which uses `localStorage` purely so every screen is interactive out of the box. To wire this to your real Firebase project:

1. Add your Firebase config + SDK `<script>` tags (or bundle) to each page (or a shared `firebase-init.js`).
2. Replace `HDIMS.db.get()` in `assets/js/app.js` with real Firestore reads (`getDocs`, `onSnapshot`, etc.).
3. Replace the `setTimeout(...)` fake-submit logic in the auth forms (`login-*.html`, `register-*.html`) with real `signInWithEmailAndPassword` / `createUserWithEmailAndPassword` / phone-OTP `signInWithPhoneNumber` calls.
4. Replace the simulated upload progress in `patient/records.html` with real Firebase Storage `uploadBytesResumable`, using its `on('state_changed', ...)` progress callback to drive the same `.progress-bar` UI already in place.
5. Wire the Approve/Reject/Generate-OTP/Verify buttons across `patient/access.html` and `doctor/access.html` to your real access-request and OTP Cloud Functions — the UI states (Not Authorized → Pending → OTP → Active countdown → Expired) are already built; they just need real data driving them.

## Structure
```
index.html                landing page
login-patient.html, register-patient.html
login-doctor.html,  register-doctor.html
login-admin.html
patient/   dashboard, family, records, doctors, appointments,
           access, prescriptions, ai-health, notifications, settings
doctor/    dashboard, patients, access, appointments,
           prescriptions, notifications, settings
admin/     dashboard, verify, patients, access, analytics, settings
assets/css/style.css       full design system (tokens, components, dark mode, responsive)
assets/js/app.js           theme, sidebar, toasts, OTP inputs, countdowns, i18n, mock data
_generator/                the Python scripts used to generate the dashboard-shell pages
                           consistently (safe to ignore/delete — not needed to run the site)
```

## Design system
- **Colors:** deep navy `#0B1220` / `#102A43`, medical blue `#1D6FE0`, sky accent `#38BDF8`, teal `#14B8A6`, mist background `#F4F8FC`.
- **Type:** Manrope for headings, Inter for body/UI.
- **Dark mode:** toggle in every topbar/settings page, persisted in `localStorage`.
- **Language:** EN / HI / MR selector wired to a small dictionary in `app.js` (extend `dict` for full coverage).
