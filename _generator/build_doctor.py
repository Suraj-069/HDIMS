# -*- coding: utf-8 -*-
from build import page, write, icon

# ---------------------------------------------------------------- dashboard
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Good morning, Dr. Sharma</h1><p>Here's what's on your schedule today.</p></div></div>

<div class="stat-grid">
  <div class="card stat-card card-hover"><div class="stat-icon">{a1}</div><div><div class="stat-value">6</div><div class="stat-label">Today's Appointments</div></div></div>
  <div class="card stat-card card-hover"><div class="stat-icon">{a2}</div><div><div class="stat-value">2</div><div class="stat-label">Pending Requests</div></div></div>
  <div class="card stat-card card-hover"><div class="stat-icon">{a3}</div><div><div class="stat-value">184</div><div class="stat-label">Total Patients</div></div></div>
  <div class="card stat-card card-hover"><div class="stat-icon">{a4}</div><div><div class="stat-value">1</div><div class="stat-label">Active Access Sessions</div></div></div>
</div>

<div class="grid-2">
  <div class="card" style="padding:24px;">
    <h3>Today's Schedule</h3>
    <div class="timeline" style="margin-top:18px;">
      <div class="timeline-item"><span class="text-sm text-soft" style="font-weight:700;">10:00 AM</span><p style="color:var(--text);margin:2px 0 6px;">Amit Sharma — General Consultation</p><span class="badge badge-confirmed">Confirmed</span></div>
      <div class="timeline-item"><span class="text-sm text-soft" style="font-weight:700;">10:30 AM</span><p style="color:var(--text);margin:2px 0 6px;">Priya Patil — Follow-up</p><span class="badge badge-pending">Pending</span></div>
      <div class="timeline-item"><span class="text-sm text-soft" style="font-weight:700;">11:15 AM</span><p style="color:var(--text);margin:2px 0 6px;">Rakesh Jain — New Patient</p><span class="badge badge-confirmed">Confirmed</span></div>
      <div class="timeline-item"><span class="text-sm text-soft" style="font-weight:700;">2:00 PM</span><p style="color:var(--text);margin:2px 0 6px;">Sunita Sharma — Annual Checkup</p><span class="badge badge-completed">Completed</span></div>
    </div>
  </div>
  <div class="flex" style="flex-direction:column;gap:20px;">
    <div class="card" style="padding:20px;">
      <div class="flex justify-between items-center mb-0"><h3 class="mb-0">Active Medical Access</h3><span class="badge badge-active">Active</span></div>
      <p style="margin:10px 0 0;">Amit Sharma · Blood Reports, Prescriptions</p>
      <p class="text-sm" style="margin:2px 0 0;">Expires in 00:47:32</p>
    </div>
    <div class="card" style="padding:20px;">
      <div class="flex justify-between items-center mb-0"><h3 class="mb-0">Pending Access Request</h3><span class="badge badge-pending">Waiting</span></div>
      <p style="margin:10px 0 0;">Priya Patil — request sent 10 min ago</p>
      <a href="access.html" class="btn btn-secondary btn-sm" style="margin-top:10px;">View Request</a>
    </div>
  </div>
</div>
'''.format(a1=icon('appointments'), a2=icon('access'), a3=icon('patients'), a4=icon('shield'))
write('doctor', 'dashboard.html', page('doctor','dashboard.html','Dashboard',"Today's schedule at a glance.", content))

# ---------------------------------------------------------------- patients
rows = [
  ('Amit Sharma','PAT-2026-000123','26 Sep, 10:00 AM','Confirmed','Not Authorized'),
  ('Priya Patil','PAT-2026-000456','26 Sep, 10:30 AM','Pending','Not Authorized'),
  ('Rakesh Jain','PAT-2025-000789','26 Sep, 11:15 AM','Confirmed','Authorized (47:32 left)'),
  ('Sunita Sharma','PAT-2024-000234','02 Sep, 2:00 PM','Completed','Not Authorized'),
]
trs = ''
for name, pid, appt, status, access in rows:
    badge = {'Confirmed':'badge-confirmed','Pending':'badge-pending','Completed':'badge-completed'}[status]
    access_badge = 'badge-active' if access.startswith('Authorized') else 'badge-notauth'
    trs += '''<tr>
      <td>{name}</td><td class="text-sm">{pid} <button class="copy-btn" data-copy="{pid}">{copy}</button></td>
      <td>{appt}</td><td><span class="badge {badge}">{status}</span></td>
      <td><span class="badge {access_badge}">{access}</span></td>
      <td><a href="access.html" class="btn btn-ghost btn-sm">Manage Access</a></td>
    </tr>'''.format(name=name, pid=pid, appt=appt, status=status, badge=badge, access=access, access_badge=access_badge,
                     copy='<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15V5a2 2 0 012-2h10"/></svg>')

content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">My Patients</h1><p>Patients you have appointments with or have treated before.</p></div></div>

<div class="card" style="padding:16px 20px;margin-bottom:16px;background:var(--surface-2);">
  <p class="text-sm mb-0">ℹ️ Seeing a patient's name or ID here does not grant access to their medical records. You must request and receive authorized access separately.</p>
</div>

<div class="card table-wrap">
  <table class="data-table">
    <thead><tr><th>Patient</th><th>Patient ID</th><th>Appointment</th><th>Status</th><th>Record Access</th><th>Action</th></tr></thead>
    <tbody>{trs}</tbody>
  </table>
</div>
'''.format(trs=trs)
write('doctor', 'patients.html', page('doctor','patients.html','My Patients','Appointments and record-access status.', content))

# ---------------------------------------------------------------- access requests (request / OTP entry / active / walk-in)
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Access Requests</h1><p>Request, verify and monitor patient record access.</p></div></div>

<div class="access-banner" style="margin-bottom:26px;">
  <div class="abrow">
    <div>
      <span class="badge" style="background:rgba(255,255,255,.14);color:#fff;">ACTIVE MEDICAL ACCESS</span>
      <h3 style="color:#fff;margin:12px 0 4px;">Amit Sharma</h3>
      <p style="color:#B9C6DA;margin:0;">Patient ID: PAT-2026-000123</p>
      <div class="flex gap-16" style="margin-top:14px;">
        <span class="text-sm" style="color:#B9C6DA;">✓ Medical Reports</span>
        <span class="text-sm" style="color:#B9C6DA;">✓ Prescriptions</span>
        <span class="text-sm" style="color:#B9C6DA;">✓ Diagnosis History</span>
      </div>
    </div>
    <div style="text-align:right;">
      <div class="text-sm" style="color:#B9C6DA;margin-bottom:6px;">Access expires in</div>
      <div class="countdown" id="accessTimer" style="color:#fff;">00:47:32</div>
    </div>
  </div>
</div>

<div class="grid-2">
  <div class="card" style="padding:22px;">
    <h3>Request Record Access</h3>
    <div class="flex justify-between text-sm" style="padding:14px 0;border-bottom:1px solid var(--border);"><span class="text-soft">Patient</span><span>Priya Patil</span></div>
    <div class="flex justify-between text-sm" style="padding:14px 0;border-bottom:1px solid var(--border);"><span class="text-soft">Patient ID</span><span>PAT-2026-000456 <button class="copy-btn" data-copy="PAT-2026-000456">⧉</button></span></div>
    <div class="flex justify-between text-sm" style="padding:14px 0;"><span class="text-soft">Access Status</span><span class="badge badge-notauth">Not Authorized</span></div>
    <div class="field" style="margin-top:6px;"><label>Reason for Access</label><input class="input" placeholder="e.g. Follow-up consultation"></div>
    <button class="btn btn-primary btn-block" onclick="HDIMS.toast('Access request sent to patient','success')">Request Record Access</button>
  </div>

  <div class="card" style="padding:22px;">
    <h3>Walk-in / Direct Visit Access</h3>
    <p class="text-sm">For patients visiting without a prior appointment. Ask the patient to generate an OTP from their app, then enter it below.</p>
    <div class="field"><label>Patient ID</label><input class="input" placeholder="e.g. PAT-2026-000789"></div>
    <div class="field"><label>Enter OTP</label>
      <div class="otp-row" style="justify-content:flex-start;">
        <input class="otp-box" style="width:40px;height:46px;" maxlength="1"><input class="otp-box" style="width:40px;height:46px;" maxlength="1"><input class="otp-box" style="width:40px;height:46px;" maxlength="1">
        <input class="otp-box" style="width:40px;height:46px;" maxlength="1"><input class="otp-box" style="width:40px;height:46px;" maxlength="1"><input class="otp-box" style="width:40px;height:46px;" maxlength="1">
      </div>
    </div>
    <button class="btn btn-primary btn-block" onclick="HDIMS.toast('Access verified — records unlocked','success')">Verify Access</button>
  </div>
</div>

<div class="section-head" style="margin-top:30px;"><h2>Recent Requests</h2></div>
<div class="card table-wrap">
  <table class="data-table">
    <thead><tr><th>Patient</th><th>Requested</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Priya Patil</td><td>10 min ago</td><td><span class="badge badge-pending">Waiting for approval</span></td></tr>
      <tr><td>Amit Sharma</td><td>Today, 9:14 AM</td><td><span class="badge badge-active">Approved &amp; Active</span></td></tr>
      <tr><td>Sunita Sharma</td><td>Yesterday</td><td><span class="badge badge-notauth">Expired</span></td></tr>
    </tbody>
  </table>
</div>
'''
write('doctor', 'access.html', page('doctor','access.html','Access Requests','Request, verify and monitor patient access.', content,
     extra_script='<script>document.addEventListener("DOMContentLoaded",function(){HDIMS.startCountdown(document.getElementById("accessTimer"),2852);});</script>'))

# ---------------------------------------------------------------- appointments
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Appointments</h1><p>Manage your upcoming and past consultations.</p></div></div>
<div class="card table-wrap">
  <table class="data-table">
    <thead><tr><th>Patient</th><th>Date</th><th>Time</th><th>Reason</th><th>Status</th><th>Action</th></tr></thead>
    <tbody>
      <tr><td>Amit Sharma</td><td>26 Sep 2026</td><td>10:00 AM</td><td>General Consultation</td><td><span class="badge badge-confirmed">Confirmed</span></td><td><button class="btn btn-ghost btn-sm">View</button></td></tr>
      <tr><td>Priya Patil</td><td>26 Sep 2026</td><td>10:30 AM</td><td>Follow-up</td><td><span class="badge badge-pending">Pending</span></td><td><button class="btn btn-secondary btn-sm" onclick="HDIMS.toast('Appointment accepted','success')">Accept</button> <button class="btn btn-ghost btn-sm" onclick="HDIMS.toast('Appointment declined','error')">Decline</button></td></tr>
      <tr><td>Sunita Sharma</td><td>02 Sep 2026</td><td>2:00 PM</td><td>Annual Checkup</td><td><span class="badge badge-completed">Completed</span></td><td><button class="btn btn-ghost btn-sm">View</button></td></tr>
      <tr><td>Rakesh Jain</td><td>18 Aug 2026</td><td>11:00 AM</td><td>New Patient</td><td><span class="badge badge-cancelled">Cancelled</span></td><td><button class="btn btn-ghost btn-sm">View</button></td></tr>
    </tbody>
  </table>
</div>
'''
write('doctor', 'appointments.html', page('doctor','appointments.html','Appointments','Confirm, decline and track consultations.', content))

# ---------------------------------------------------------------- prescriptions
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Prescriptions</h1><p>Issue and track prescriptions for authorized patients.</p></div>
<button class="btn btn-primary" onclick="document.getElementById('rxModal').classList.add('open')">+ New Prescription</button></div>
<div class="card table-wrap">
  <table class="data-table">
    <thead><tr><th>Patient</th><th>Medication</th><th>Date Issued</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Amit Sharma</td><td>Amoxicillin 500mg</td><td>02 Aug 2026</td><td><span class="badge badge-active">Active</span></td></tr>
      <tr><td>Sunita Sharma</td><td>Vitamin D3</td><td>02 Sep 2026</td><td><span class="badge badge-active">Active</span></td></tr>
    </tbody>
  </table>
</div>
<div class="modal-overlay" id="rxModal">
  <div class="modal">
    <h3>New Prescription</h3>
    <div class="field"><label>Patient</label><select class="input"><option>Amit Sharma (Access Active)</option></select></div>
    <div class="field"><label>Medication</label><input class="input" placeholder="e.g. Amoxicillin 500mg"></div>
    <div class="field"><label>Dosage &amp; Instructions</label><textarea class="input" rows="3" placeholder="e.g. 1 tablet, twice daily for 5 days"></textarea></div>
    <div class="flex gap-12"><button class="btn btn-secondary btn-block" onclick="document.getElementById('rxModal').classList.remove('open')">Cancel</button>
    <button class="btn btn-primary btn-block" onclick="HDIMS.toast('Prescription issued','success');document.getElementById('rxModal').classList.remove('open')">Issue Prescription</button></div>
  </div>
</div>
'''
write('doctor', 'prescriptions.html', page('doctor','prescriptions.html','Prescriptions','Issued to patients with active access.', content))

# ---------------------------------------------------------------- notifications & settings (reuse patient style content)
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Notifications</h1><p>Requests, appointments and account activity.</p></div></div>
<div class="card" style="padding:8px 20px;">
  <div class="flex gap-12" style="padding:16px 4px;border-bottom:1px solid var(--border);background:var(--surface-2);">
    <span style="width:8px;height:8px;border-radius:50%;margin-top:6px;background:var(--blue);"></span>
    <div style="flex:1;"><div class="flex justify-between"><b class="text-sm">New appointment request</b><span class="text-sm text-soft">10m ago</span></div>
    <p class="text-sm" style="margin:4px 0 0;">Priya Patil requested a follow-up appointment.</p></div>
  </div>
  <div class="flex gap-12" style="padding:16px 4px;border-bottom:1px solid var(--border);">
    <span style="width:8px;height:8px;border-radius:50%;margin-top:6px;"></span>
    <div style="flex:1;"><div class="flex justify-between"><b class="text-sm">Access approved</b><span class="text-sm text-soft">Today, 9:14 AM</span></div>
    <p class="text-sm" style="margin:4px 0 0;">Amit Sharma approved your record access request.</p></div>
  </div>
  <div class="flex gap-12" style="padding:16px 4px;">
    <span style="width:8px;height:8px;border-radius:50%;margin-top:6px;"></span>
    <div style="flex:1;"><div class="flex justify-between"><b class="text-sm">Verification complete</b><span class="text-sm text-soft">3 days ago</span></div>
    <p class="text-sm" style="margin:4px 0 0;">Your doctor account was verified by an HDIMS admin.</p></div>
  </div>
</div>
'''
write('doctor', 'notifications.html', page('doctor','notifications.html','Notifications','Stay on top of your practice.', content))

content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Settings</h1><p>Manage your profile and clinic preferences.</p></div></div>
<div class="grid-2">
  <div class="card" style="padding:22px;">
    <h3>Profile</h3>
    <div class="field"><label>Full Name</label><input class="input" value="Dr. Rahul Sharma"></div>
    <div class="field"><label>Specialization</label><input class="input" value="General Physician"></div>
    <div class="field mb-0"><label>Medical Registration No.</label><input class="input" value="MH/2014/0091234" disabled></div>
    <button class="btn btn-primary btn-sm" style="margin-top:6px;">Save Changes</button>
  </div>
  <div class="card" style="padding:22px;">
    <h3>Preferences</h3>
    <div class="flex justify-between items-center" style="padding:10px 0;border-bottom:1px solid var(--border);"><span class="text-sm">Appearance</span>
      <button class="toggle-pill" data-theme-toggle><span class="t-label">Light</span></button></div>
    <div class="flex justify-between items-center" style="padding:10px 0;"><span class="text-sm">Language</span>
      <select class="lang-select" data-lang-select><option value="en">English</option><option value="hi">हिंदी</option><option value="mr">मराठी</option></select></div>
  </div>
</div>
'''
write('doctor', 'settings.html', page('doctor','settings.html','Settings','Your account, your practice.', content))

print('doctor pages: access, appointments, prescriptions, notifications, settings done')

