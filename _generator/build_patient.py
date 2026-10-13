# -*- coding: utf-8 -*-
from build import page, write, icon

# ---------------------------------------------------------------- dashboard
content = '''
<div class="section-head">
  <div>
    <h1 style="font-size:1.9rem;">Good morning, Amit</h1>
    <p>Here's your health overview for today. <span class="text-soft">Patient ID:</span> <b>PAT-2026-000123</b>
      <button class="copy-btn" data-copy="PAT-2026-000123" title="Copy Patient ID">{copy}</button>
    </p>
  </div>
  <a href="records.html" class="btn btn-primary">{upload_icon} Upload Record</a>
</div>

<div class="stat-grid">
  <div class="card stat-card card-hover">
    <div class="stat-icon">{records_icon}</div>
    <div><div class="stat-value">14</div><div class="stat-label">Medical Records</div></div>
  </div>
  <div class="card stat-card card-hover">
    <div class="stat-icon">{family_icon}</div>
    <div><div class="stat-value">4</div><div class="stat-label">Family Members</div></div>
  </div>
  <div class="card stat-card card-hover">
    <div class="stat-icon">{appt_icon}</div>
    <div><div class="stat-value">2</div><div class="stat-label">Upcoming Appointments</div></div>
  </div>
  <div class="card stat-card card-hover">
    <div class="stat-icon">{access_icon}</div>
    <div><div class="stat-value">1</div><div class="stat-label">Active Access</div></div>
  </div>
</div>

<div class="section-head"><h2>Health Overview</h2></div>
<div class="grid-2">
  <div class="card" style="padding:24px;">
    <h3>Recent Activity</h3>
    <div class="timeline" style="margin-top:18px;">
      <div class="timeline-item"><span class="text-sm text-soft">Today, 9:02 AM</span><p style="margin:2px 0 0;color:var(--text);">Dr. Rahul Sharma requested access to your records</p></div>
      <div class="timeline-item"><span class="text-sm text-soft">Yesterday</span><p style="margin:2px 0 0;color:var(--text);">Blood Test Report uploaded for Amit Sharma</p></div>
      <div class="timeline-item"><span class="text-sm text-soft">3 days ago</span><p style="margin:2px 0 0;color:var(--text);">Appointment confirmed with Dr. Neha Kulkarni</p></div>
    </div>
  </div>
  <div class="flex" style="flex-direction:column;gap:20px;">
    <div class="card" style="padding:20px;">
      <div class="flex justify-between items-center mb-0"><h3 class="mb-0">Upcoming Appointment</h3><span class="badge badge-confirmed">Confirmed</span></div>
      <p style="margin:10px 0 0;">Dr. Rahul Sharma · General Consultation</p>
      <p class="text-sm" style="margin:2px 0 0;">26 Sep 2026, 10:00 AM</p>
    </div>
    <div class="card" style="padding:20px;">
      <div class="flex justify-between items-center mb-0"><h3 class="mb-0">Active Doctor Access</h3><span class="badge badge-active">Active</span></div>
      <p style="margin:10px 0 0;">Dr. Rahul Sharma can view Blood Reports, Prescriptions</p>
      <p class="text-sm" style="margin:2px 0 0;">Expires in 00:47:32</p>
    </div>
  </div>
</div>
'''.format(copy=icon('records',14), upload_icon=icon('records',16), records_icon=icon('records'),
           family_icon=icon('family'), appt_icon=icon('appointments'), access_icon=icon('access'))

write('patient', 'dashboard.html', page('patient','dashboard.html','Dashboard','Your health, organized.', content))

# ---------------------------------------------------------------- family
fam_cards = ''
members = [
  ('SELF','Amit Sharma','14','2 days ago'),
  ('MOTHER','Sunita Sharma','9','1 week ago'),
  ('FATHER','Rajesh Sharma','22','3 weeks ago'),
  ('GRANDMOTHER','Kamala Devi','5','2 months ago'),
]
for rel, name, records, updated in members:
    initials = ''.join([p[0] for p in name.split()[:2]])
    fam_cards += '''
    <div class="card profile-card card-hover">
      <div class="flex items-center gap-12">
        <span class="avatar">{initials}</span>
        <div><b>{name}</b><div class="text-sm text-soft">{rel}</div></div>
      </div>
      <div class="flex justify-between text-sm text-soft" style="border-top:1px solid var(--border);padding-top:12px;">
        <span>{records} records</span><span>Updated {updated}</span>
      </div>
      <a href="records.html" class="btn btn-secondary btn-sm btn-block">View Records</a>
    </div>'''.format(initials=initials, name=name, rel=rel, records=records, updated=updated)

content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">My Family</h1><p>Manage medical records for every family member in one place.</p></div>
<button class="btn btn-primary" onclick="document.getElementById('addFamily').classList.add('open')">+ Add Family Member</button></div>
<div class="stat-grid" style="grid-template-columns:repeat(4,1fr);">{cards}</div>

<div class="modal-overlay" id="addFamily">
  <div class="modal">
    <h3>Add Family Member</h3>
    <div class="field"><label>Full Name</label><input class="input" placeholder="e.g. Priya Sharma"></div>
    <div class="field"><label>Relationship</label>
      <select class="input"><option>Spouse</option><option>Child</option><option>Mother</option><option>Father</option><option>Sibling</option><option>Grandparent</option></select>
    </div>
    <div class="field"><label>Date of Birth</label><input class="input" type="date"></div>
    <div class="flex gap-12"><button class="btn btn-secondary btn-block" onclick="document.getElementById('addFamily').classList.remove('open')">Cancel</button>
    <button class="btn btn-primary btn-block" onclick="HDIMS.toast('Family member added','success');document.getElementById('addFamily').classList.remove('open')">Add Member</button></div>
  </div>
</div>
'''.format(cards=fam_cards)
write('patient', 'family.html', page('patient','family.html','My Family','Every family member, one record.', content))

# ---------------------------------------------------------------- records
records = [
  ('Blood Test Report.pdf','PDF','12 Sep 2026','Annual Checkup','Fasting sugar normal','Amit Sharma'),
  ('Chest X-Ray.jpg','Image','02 Aug 2026','Cough & Fever','No abnormality found','Amit Sharma'),
  ('Prescription - Dr. Rahul.pdf','PDF','02 Aug 2026','Follow-up','5 day antibiotic course','Amit Sharma'),
  ('MRI Scan Report.pdf','Report','19 Jun 2026','Knee Pain','Mild ligament strain','Rajesh Sharma'),
]
FILE_ICON = {
 'PDF': '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/>',
 'Image': '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/>',
 'Report': '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/><path d="M9 13h6M9 17h6"/>',
}
def file_icon(t): return '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{}</svg>'.format(FILE_ICON[t])

rows = ''
cards = ''
for doc, t, date, issue, notes, member in records:
    rows += '''<tr>
      <td class="flex items-center gap-12">{icon}<span>{doc}</span></td>
      <td>{date}</td><td>{issue}</td><td class="text-soft text-sm">{notes}</td>
      <td><button class="btn btn-ghost btn-sm">View</button><button class="btn btn-ghost btn-sm">Download</button></td>
    </tr>'''.format(icon=file_icon(t), doc=doc, date=date, issue=issue, notes=notes)
    cards += '''<div class="card" style="padding:16px;">
      <div class="flex items-center gap-12 justify-between">
        <div class="flex items-center gap-12">{icon}<div><b class="text-sm">{doc}</b><div class="text-sm text-soft">{issue} · {date}</div></div></div>
      </div>
    </div>'''.format(icon=file_icon(t), doc=doc, issue=issue, date=date)

content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Medical Records</h1><p>Every report, prescription and scan — searchable in one place.</p></div>
<button class="btn btn-primary" onclick="document.getElementById('uploadModal').classList.add('open')">+ Upload Record</button></div>

<div class="card" style="padding:16px 20px;margin-bottom:20px;">
  <div class="flex gap-12" style="flex-wrap:wrap;">
    <input class="input" style="max-width:260px;" placeholder="Search records...">
    <select class="input" style="max-width:180px;"><option>All Family Members</option><option>Amit Sharma</option><option>Sunita Sharma</option><option>Rajesh Sharma</option></select>
    <select class="input" style="max-width:160px;"><option>All Types</option><option>PDF</option><option>Image</option><option>Report</option></select>
    <select class="input" style="max-width:160px;"><option>All Dates</option><option>Last 30 days</option><option>This Year</option></select>
  </div>
</div>

<div class="card table-wrap">
  <table class="data-table">
    <thead><tr><th>Document</th><th>Date</th><th>Health Issue</th><th>Notes</th><th>Actions</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>
<div class="record-cards">{cards}</div>

<div class="modal-overlay" id="uploadModal">
  <div class="modal" style="max-width:460px;">
    <h3>Upload Medical Record</h3>
    <div class="field"><label>Family Member</label><select class="input"><option>Amit Sharma (Self)</option><option>Sunita Sharma</option><option>Rajesh Sharma</option></select></div>
    <div class="field"><label>Health Issue</label><input class="input" placeholder="e.g. Annual Checkup"></div>
    <div class="dropzone" data-dropzone data-progress-target="#uploadProgress">
      <input type="file" hidden>
      {upload_icon}
      <p style="margin:10px 0 4px;font-weight:600;color:var(--text);">Drag &amp; Drop your report</p>
      <p class="text-sm">or <b style="color:var(--blue)">Browse Files</b> — PDF, JPG, PNG</p>
    </div>
    <div id="uploadProgress" style="display:none;margin-top:14px;">
      <div class="progress-label text-sm text-soft"></div>
      <div class="progress-bar"><div></div></div>
    </div>
    <div class="flex gap-12" style="margin-top:20px;">
      <button class="btn btn-secondary btn-block" onclick="document.getElementById('uploadModal').classList.remove('open')">Cancel</button>
      <button class="btn btn-primary btn-block" onclick="document.getElementById('uploadModal').classList.remove('open')">Save Record</button>
    </div>
  </div>
</div>
'''.format(rows=rows, cards=cards, upload_icon='<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="margin:0 auto;color:var(--blue);"><path d="M12 16V4M12 4l-4 4M12 4l4 4"/><path d="M4 16v3a2 2 0 002 2h12a2 2 0 002-2v-3"/></svg>')
write('patient', 'records.html', page('patient','records.html','Medical Records','All reports, in one searchable place.', content))

# ---------------------------------------------------------------- doctors
doctor_cards = ''
docs = [
  ('Dr. Rahul Sharma','DOC-2024-0091','General Physician','12 yrs','Available Today'),
  ('Dr. Neha Kulkarni','DOC-2023-0042','Cardiologist','9 yrs','Next slot Tomorrow'),
  ('Dr. Arvind Menon','DOC-2022-0117','Orthopedic','15 yrs','Available Today'),
]
for name, did, spec, exp, avail in docs:
    initials = ''.join([p[0] for p in name.replace('Dr. ','').split()[:2]])
    doctor_cards += '''
    <div class="card profile-card card-hover">
      <div class="flex justify-between items-start">
        <div class="flex items-center gap-12"><span class="avatar">{initials}</span>
          <div><b>{name}</b> {badge}<div class="text-sm text-soft">{did}</div></div>
        </div>
      </div>
      <div class="text-sm" style="border-top:1px solid var(--border);padding-top:12px;">
        <div class="flex justify-between"><span class="text-soft">Specialization</span><span>{spec}</span></div>
        <div class="flex justify-between" style="margin-top:6px;"><span class="text-soft">Experience</span><span>{exp}</span></div>
        <div class="flex justify-between" style="margin-top:6px;"><span class="text-soft">Availability</span><span style="color:var(--success);">{avail}</span></div>
      </div>
      <a href="appointments.html" class="btn btn-primary btn-sm btn-block">Book Appointment</a>
    </div>'''.format(initials=initials, name=name, did=did, spec=spec, exp=exp, avail=avail,
                      badge='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#1D6FE0" stroke-width="2.4" style="display:inline;vertical-align:-2px;"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg>')

content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Find a Doctor</h1><p>Verified doctors ready to consult — book instantly or visit in person.</p></div></div>
<div class="card" style="padding:16px 20px;margin-bottom:20px;"><input class="input" placeholder="Search by name or specialization..."></div>
<div class="stat-grid" style="grid-template-columns:repeat(3,1fr);">{cards}</div>
'''.format(cards=doctor_cards)
write('patient', 'doctors.html', page('patient','doctors.html','Doctors','Verified specialists, ready to help.', content))

# ---------------------------------------------------------------- appointments
slots = ['9:00 AM','9:30 AM','10:00 AM','10:30 AM','11:00 AM','11:30 AM','2:00 PM','2:30 PM','3:00 PM','3:30 PM']
slot_html = ''
for i, s in enumerate(slots):
    cls = 'slot selected' if i==2 else ('slot taken' if i==5 else 'slot')
    slot_html += '<div class="{cls}" onclick="selectSlot(this)">{s}</div>'.format(cls=cls, s=s)

content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Book an Appointment</h1><p>Schedule a consultation in a few quick steps.</p></div></div>

<div class="stepper">
  <div class="step done"><div class="step-dot">{check}</div><div class="step-label">Doctor</div></div><div class="step-line filled"></div>
  <div class="step active"><div class="step-dot">2</div><div class="step-label">Date &amp; Time</div></div><div class="step-line"></div>
  <div class="step"><div class="step-dot">3</div><div class="step-label">Reason</div></div><div class="step-line"></div>
  <div class="step"><div class="step-dot">4</div><div class="step-label">Confirm</div></div>
</div>

<div class="grid-2">
  <div class="card" style="padding:24px;">
    <h3>Select Date</h3>
    <input class="input" type="date" style="max-width:220px;margin-bottom:22px;">
    <h3>Available Time Slots</h3>
    <div class="slot-grid" style="margin-top:14px;">{slots}</div>
    <div class="field" style="margin-top:24px;"><label>Reason for Visit</label><textarea class="input" rows="3" placeholder="Briefly describe your symptoms or reason for consultation"></textarea></div>
    <button class="btn btn-primary" style="margin-top:6px;">Continue to Confirm</button>
  </div>
  <div class="card" style="padding:22px;">
    <h3>Appointment Summary</h3>
    <div class="flex items-center gap-12" style="margin:14px 0 18px;"><span class="avatar">RS</span><div><b>Dr. Rahul Sharma</b><div class="text-sm text-soft">General Physician</div></div></div>
    <div class="text-sm" style="border-top:1px solid var(--border);padding-top:14px;">
      <div class="flex justify-between" style="margin-bottom:8px;"><span class="text-soft">Date</span><span>26 Sep 2026</span></div>
      <div class="flex justify-between"><span class="text-soft">Time</span><span>10:00 AM</span></div>
    </div>
  </div>
</div>

<div class="section-head" style="margin-top:32px;"><h2>Your Appointments</h2></div>
<div class="card table-wrap">
  <table class="data-table">
    <thead><tr><th>Doctor</th><th>Date</th><th>Time</th><th>Reason</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Dr. Rahul Sharma</td><td>26 Sep 2026</td><td>10:00 AM</td><td>General Consultation</td><td><span class="badge badge-confirmed">Confirmed</span></td></tr>
      <tr><td>Dr. Neha Kulkarni</td><td>30 Sep 2026</td><td>4:30 PM</td><td>Follow-up</td><td><span class="badge badge-pending">Pending</span></td></tr>
      <tr><td>Dr. Arvind Menon</td><td>02 Sep 2026</td><td>11:00 AM</td><td>Knee Pain</td><td><span class="badge badge-completed">Completed</span></td></tr>
    </tbody>
  </table>
</div>
'''.format(slots=slot_html, check='<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg>')

write('patient', 'appointments.html', page('patient','appointments.html','Appointments','Book and manage your consultations.', content,
     extra_script='<script>function selectSlot(el){document.querySelectorAll(".slot").forEach(s=>s.classList.remove("selected"));if(!el.classList.contains("taken"))el.classList.add("selected");}</script>'))

# ---------------------------------------------------------------- shared access (request/OTP/active/temp permissions)
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Shared Access</h1><p>Control exactly who can see your medical records, and for how long.</p></div></div>

<div class="access-banner" style="margin-bottom:26px;">
  <div class="abrow">
    <div>
      <span class="badge" style="background:rgba(255,255,255,.14);color:#fff;">ACTIVE MEDICAL ACCESS</span>
      <h3 style="color:#fff;margin:12px 0 4px;">Dr. Rahul Sharma</h3>
      <p style="color:#B9C6DA;margin:0;">Doctor ID: DOC-2024-0091</p>
      <div class="flex gap-16" style="margin-top:14px;">
        <span class="text-sm" style="color:#B9C6DA;">✓ Medical Reports</span>
        <span class="text-sm" style="color:#B9C6DA;">✓ Prescriptions</span>
        <span class="text-sm" style="color:#B9C6DA;">✓ Diagnosis History</span>
      </div>
    </div>
    <div style="text-align:right;">
      <div class="text-sm" style="color:#B9C6DA;margin-bottom:6px;">Access expires in</div>
      <div class="countdown" id="accessTimer" style="color:#fff;">00:47:32</div>
      <button class="btn btn-danger btn-sm" style="margin-top:12px;background:rgba(224,72,63,.16);border-color:transparent;color:#FCA5A0;" onclick="HDIMS.toast('Access revoked','success')">Revoke Access</button>
    </div>
  </div>
</div>

<div class="section-head"><h2>Pending Access Request</h2></div>
<div class="card" style="padding:22px;margin-bottom:28px;">
  <div class="flex justify-between items-start" style="flex-wrap:wrap;gap:16px;">
    <div class="flex items-center gap-12">
      <span class="avatar">NK</span>
      <div>
        <b>Dr. Neha Kulkarni is requesting access to your medical records.</b>
        <p class="text-sm" style="margin:6px 0 0;">Doctor ID: DOC-2023-0042 · Reason: Follow-up consultation · Appointment: 30 Sep 2026</p>
      </div>
    </div>
    <div class="flex gap-12">
      <button class="btn btn-secondary btn-sm" onclick="HDIMS.toast('Request rejected','error')">Reject</button>
      <button class="btn btn-primary btn-sm" onclick="document.getElementById('permModal').classList.add('open')">Approve</button>
    </div>
  </div>
</div>

<div class="section-head"><h2>Access History</h2></div>
<div class="card table-wrap">
  <table class="data-table">
    <thead><tr><th>Doctor</th><th>Records Shared</th><th>Duration</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Dr. Rahul Sharma</td><td>Blood Reports, Prescriptions</td><td>1 Hour</td><td><span class="badge badge-active">Active</span></td></tr>
      <tr><td>Dr. Arvind Menon</td><td>Previous Diagnosis</td><td>30 Minutes</td><td><span class="badge badge-notauth">Expired</span></td></tr>
    </tbody>
  </table>
</div>

<!-- Step 1: choose records + duration -->
<div class="modal-overlay" id="permModal">
  <div class="modal" style="max-width:440px;">
    <h3>Grant Temporary Access</h3>
    <p class="text-sm">Choose what Dr. Neha Kulkarni can view, and for how long.</p>
    <div class="field"><label>Records to Share</label>
      <div class="flex" style="flex-direction:column;gap:10px;margin-top:6px;">
        <label class="flex items-center gap-8 text-sm"><input type="checkbox" checked> Blood Reports</label>
        <label class="flex items-center gap-8 text-sm"><input type="checkbox" checked> Prescriptions</label>
        <label class="flex items-center gap-8 text-sm"><input type="checkbox" checked> Previous Diagnosis</label>
        <label class="flex items-center gap-8 text-sm"><input type="checkbox"> Personal Notes</label>
      </div>
    </div>
    <div class="field"><label>Access Duration</label>
      <select class="input"><option>30 Minutes</option><option selected>1 Hour</option><option>2 Hours</option><option>24 Hours</option></select>
    </div>
    <button class="btn btn-primary btn-block" onclick="document.getElementById('permModal').classList.remove('open');document.getElementById('otpModal').classList.add('open')">Generate Access OTP</button>
  </div>
</div>

<!-- Step 2: OTP -->
<div class="modal-overlay" id="otpModal">
  <div class="modal" style="max-width:420px;text-align:center;">
    <h3>Verify Medical Record Access</h3>
    <p class="text-sm" style="margin:0 auto 18px;">Share this OTP with Dr. Neha Kulkarni to activate access.</p>
    <div class="otp-row">
      <input class="otp-box filled" value="6" readonly><input class="otp-box filled" value="3" readonly><input class="otp-box filled" value="8" readonly>
      <input class="otp-box filled" value="4" readonly><input class="otp-box filled" value="2" readonly><input class="otp-box filled" value="1" readonly>
    </div>
    <p class="text-sm text-soft" style="margin-top:14px;">OTP expires in <span id="otpModalTimer" style="font-weight:700;color:var(--text);">09:42</span></p>
    <div class="flex gap-12" style="margin-top:18px;">
      <button class="btn btn-secondary btn-block" onclick="document.getElementById('otpModal').classList.remove('open')">Close</button>
      <button class="btn btn-primary btn-block" onclick="HDIMS.toast('Access granted to Dr. Neha Kulkarni','success');document.getElementById('otpModal').classList.remove('open')">Done</button>
    </div>
  </div>
</div>
'''
write('patient', 'access.html', page('patient','access.html','Shared Access','Approve, monitor and revoke doctor access.', content,
     extra_script='<script>document.addEventListener("DOMContentLoaded",function(){HDIMS.startCountdown(document.getElementById("accessTimer"),2852);HDIMS.startCountdown(document.getElementById("otpModalTimer"),582);});</script>'))

# ---------------------------------------------------------------- prescriptions
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Prescriptions</h1><p>Every prescription issued to you, in one place.</p></div></div>
<div class="stat-grid" style="grid-template-columns:repeat(3,1fr);">
  <div class="card" style="padding:20px;">
    <div class="flex justify-between items-center"><b>Amoxicillin 500mg</b><span class="badge badge-active">Active</span></div>
    <p class="text-sm" style="margin:8px 0 0;">Prescribed by Dr. Rahul Sharma · 02 Aug 2026</p>
    <p class="text-sm" style="margin:2px 0 0;">1 tablet, twice daily for 5 days</p>
  </div>
  <div class="card" style="padding:20px;">
    <div class="flex justify-between items-center"><b>Metformin 500mg</b><span class="badge badge-notauth">Completed</span></div>
    <p class="text-sm" style="margin:8px 0 0;">Prescribed by Dr. Neha Kulkarni · 12 Jun 2026</p>
    <p class="text-sm" style="margin:2px 0 0;">1 tablet, once daily with dinner</p>
  </div>
  <div class="card" style="padding:20px;">
    <div class="flex justify-between items-center"><b>Ibuprofen 200mg</b><span class="badge badge-notauth">Completed</span></div>
    <p class="text-sm" style="margin:8px 0 0;">Prescribed by Dr. Arvind Menon · 19 Jun 2026</p>
    <p class="text-sm" style="margin:2px 0 0;">As needed for knee pain, max 3/day</p>
  </div>
</div>
'''
write('patient', 'prescriptions.html', page('patient','prescriptions.html','Prescriptions','Current and past medication.', content))

# ---------------------------------------------------------------- ai health
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">AI Health Insights</h1><p>Understand your medical history in minutes.</p></div></div>

<div class="grid-2">
  <div class="card" style="padding:24px;">
    <h3>AI Health Timeline</h3>
    <div class="timeline" style="margin-top:20px;">
      <div class="timeline-item"><span class="timeline-year">2026</span><p style="color:var(--text);margin:2px 0 0;">Annual checkup normal · Treated for seasonal cough &amp; fever in August.</p></div>
      <div class="timeline-item"><span class="timeline-year">2025</span><p style="color:var(--text);margin:2px 0 0;">No major medical events recorded.</p></div>
      <div class="timeline-item"><span class="timeline-year">2024</span><p style="color:var(--text);margin:2px 0 0;">Diagnosed with mild seasonal allergies, managed with antihistamines.</p></div>
      <div class="timeline-item"><span class="timeline-year">2023</span><p style="color:var(--text);margin:2px 0 0;">Routine vaccination and general health screening.</p></div>
      <div class="timeline-item"><span class="timeline-year">2022</span><p style="color:var(--text);margin:2px 0 0;">First record added to HDIMS — baseline health profile created.</p></div>
    </div>
  </div>
  <div class="card" style="padding:24px;">
    <h3>AI Health Summary</h3>
    <p class="text-sm" style="margin-top:10px;"><b style="color:var(--text);">Key Health Events</b><br>One respiratory illness (Aug 2026), fully recovered. No hospitalizations on record.</p>
    <p class="text-sm"><b style="color:var(--text);">Medical History</b><br>No chronic conditions currently on record. Seasonal allergies noted in 2024.</p>
    <p class="text-sm"><b style="color:var(--text);">Medication History</b><br>Short-term antibiotic and antihistamine courses; no long-term medication.</p>
    <p class="text-sm" style="margin-bottom:0;"><b style="color:var(--text);">Recent Records</b><br>3 records added in the last 90 days, most recently a blood test report.</p>
  </div>
</div>

<div class="card" style="padding:16px 20px;margin-top:20px;background:var(--surface-2);">
  <p class="text-sm mb-0">⚠️ AI-generated information is for informational purposes only and is not a medical diagnosis. Always consult your doctor.</p>
</div>
'''
write('patient', 'ai-health.html', page('patient','ai-health.html','AI Health','Your history, summarized.', content))

# ---------------------------------------------------------------- notifications
def notif(title, body, time, cat, unread=False):
    dot = 'style="background:var(--blue);"' if unread else 'style="background:transparent;"'
    bg = 'background:var(--surface-2);' if unread else ''
    return '''<div class="flex gap-12" style="padding:16px 4px;border-bottom:1px solid var(--border);{bg}">
      <span style="width:8px;height:8px;border-radius:50%;margin-top:6px;{dot}"></span>
      <div style="flex:1;"><div class="flex justify-between"><b class="text-sm">{title}</b><span class="text-sm text-soft">{time}</span></div>
      <p class="text-sm" style="margin:4px 0 0;">{body}</p><span class="badge badge-notauth" style="margin-top:8px;">{cat}</span></div>
    </div>'''.format(title=title, body=body, time=time, cat=cat, dot=dot, bg=bg)

content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Notifications</h1><p>Stay on top of access requests, appointments and account activity.</p></div>
<button class="btn btn-ghost btn-sm">Mark all as read</button></div>
<div class="card" style="padding:8px 20px;">
{n1}{n2}{n3}{n4}
</div>
'''.format(
 n1=notif('Access request from Dr. Neha Kulkarni','She is requesting access to your medical records for a follow-up.','2m ago','Medical Access', True),
 n2=notif('Appointment confirmed','Your appointment with Dr. Rahul Sharma is confirmed for 26 Sep, 10:00 AM.','1h ago','Appointments', True),
 n3=notif('New prescription added','Dr. Rahul Sharma added a new prescription to your record.','Yesterday','Prescriptions'),
 n4=notif('Security alert','A new device logged into your account.','3 days ago','Security'),
)
write('patient', 'notifications.html', page('patient','notifications.html','Notifications','Everything that needs your attention.', content))

# ---------------------------------------------------------------- settings
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Settings</h1><p>Manage your profile, security and preferences.</p></div></div>
<div class="grid-2">
  <div class="flex" style="flex-direction:column;gap:20px;">
    <div class="card" style="padding:22px;">
      <h3>Profile</h3>
      <div class="field"><label>Full Name</label><input class="input" value="Amit Sharma"></div>
      <div class="field"><label>Email</label><input class="input" value="amit.sharma@email.com"></div>
      <div class="field mb-0"><label>Phone Number</label><input class="input" value="+91 98765 43210"></div>
      <button class="btn btn-primary btn-sm" style="margin-top:6px;">Save Changes</button>
    </div>
    <div class="card" style="padding:22px;">
      <h3>Password &amp; Security</h3>
      <div class="field"><label>Current Password</label><input class="input" type="password" placeholder="••••••••"></div>
      <div class="field mb-0"><label>New Password</label><input class="input" type="password" placeholder="••••••••"></div>
      <button class="btn btn-secondary btn-sm" style="margin-top:6px;">Update Password</button>
    </div>
  </div>
  <div class="flex" style="flex-direction:column;gap:20px;">
    <div class="card" style="padding:22px;">
      <h3>Preferences</h3>
      <div class="flex justify-between items-center" style="padding:10px 0;border-bottom:1px solid var(--border);"><span class="text-sm">Appearance</span>
        <button class="toggle-pill" data-theme-toggle><span class="t-label">Light</span></button></div>
      <div class="flex justify-between items-center" style="padding:10px 0;"><span class="text-sm">Language</span>
        <select class="lang-select" data-lang-select><option value="en">English</option><option value="hi">हिंदी</option><option value="mr">मराठी</option></select></div>
    </div>
    <div class="card" style="padding:22px;">
      <h3>Notifications</h3>
      <label class="flex justify-between items-center text-sm" style="padding:8px 0;"><span>Appointment reminders</span><input type="checkbox" checked></label>
      <label class="flex justify-between items-center text-sm" style="padding:8px 0;"><span>Access requests</span><input type="checkbox" checked></label>
      <label class="flex justify-between items-center text-sm" style="padding:8px 0;"><span>Product updates</span><input type="checkbox"></label>
    </div>
    <div class="card" style="padding:22px;">
      <h3>Access Permissions</h3>
      <p class="text-sm">Manage which doctors currently have access to your records.</p>
      <a href="access.html" class="btn btn-secondary btn-sm">View Shared Access</a>
    </div>
  </div>
</div>
'''
write('patient', 'settings.html', page('patient','settings.html','Settings','Your account, your rules.', content))

print('patient pages: notifications, settings done')



