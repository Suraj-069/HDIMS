# -*- coding: utf-8 -*-
from build import page, write, icon

# ---------------------------------------------------------------- dashboard
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Control Center</h1><p>Platform-wide overview and health.</p></div></div>
<div class="stat-grid">
  <div class="card stat-card card-hover"><div class="stat-icon">{i1}</div><div><div class="stat-value">12,480</div><div class="stat-label">Total Patients</div></div></div>
  <div class="card stat-card card-hover"><div class="stat-icon">{i2}</div><div><div class="stat-value">642</div><div class="stat-label">Total Doctors</div></div></div>
  <div class="card stat-card card-hover"><div class="stat-icon">{i3}</div><div><div class="stat-value">18</div><div class="stat-label">Pending Verification</div></div></div>
  <div class="card stat-card card-hover"><div class="stat-icon">{i4}</div><div><div class="stat-value">3,204</div><div class="stat-label">Appointments (30d)</div></div></div>
</div>
<div class="grid-2">
  <div class="card" style="padding:24px;">
    <h3>Active Access Sessions</h3>
    <div class="table-wrap" style="margin-top:14px;">
      <table class="data-table">
        <thead><tr><th>Doctor</th><th>Patient</th><th>Expires In</th></tr></thead>
        <tbody>
          <tr><td>Dr. Rahul Sharma</td><td>Amit Sharma</td><td>00:47:32</td></tr>
          <tr><td>Dr. Arvind Menon</td><td>Rajesh Sharma</td><td>01:12:05</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="card" style="padding:24px;">
    <h3>Platform Activity</h3>
    <div class="timeline" style="margin-top:18px;">
      <div class="timeline-item"><span class="text-sm text-soft">2m ago</span><p style="color:var(--text);margin:2px 0 0;">Dr. Neha Kulkarni's verification submitted for review</p></div>
      <div class="timeline-item"><span class="text-sm text-soft">1h ago</span><p style="color:var(--text);margin:2px 0 0;">142 new records uploaded across the platform</p></div>
      <div class="timeline-item"><span class="text-sm text-soft">Today</span><p style="color:var(--text);margin:2px 0 0;">3 access sessions expired automatically</p></div>
    </div>
  </div>
</div>
'''.format(i1=icon('patients'), i2=icon('doctors'), i3=icon('verify'), i4=icon('appointments'))
write('admin', 'dashboard.html', page('admin','dashboard.html','Overview','Platform-wide health and activity.', content))

# ---------------------------------------------------------------- doctor verification
rows = [
  ('Dr. Neha Kulkarni','DOC-2026-0512','Cardiologist','MH/2017/0055213','Pending'),
  ('Dr. Suresh Iyer','DOC-2026-0513','Dermatologist','KA/2015/0032871','Pending'),
  ('Dr. Farah Khan','DOC-2026-0514','Pediatrician','DL/2019/0071122','Pending'),
]
trs = ''
for name, did, spec, reg, status in rows:
    trs += '''<tr>
      <td>{name}</td><td class="text-sm">{did}</td><td>{spec}</td><td class="text-sm">{reg}</td>
      <td><span class="badge badge-pending">{status}</span></td>
      <td><button class="btn btn-ghost btn-sm">View</button>
      <button class="btn btn-sm" style="background:rgba(28,154,108,.12);color:var(--success);border:none;" onclick="HDIMS.toast('{name} approved','success');this.closest('tr').style.opacity=.4;">Approve</button>
      <button class="btn btn-ghost btn-sm" style="color:var(--danger);" onclick="HDIMS.toast('{name} rejected','error');this.closest('tr').style.opacity=.4;">Reject</button></td>
    </tr>'''.format(name=name, did=did, spec=spec, reg=reg, status=status)

content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Doctor Verification</h1><p>Review pending registrations before doctors can request patient access.</p></div></div>
<div class="card table-wrap">
  <table class="data-table">
    <thead><tr><th>Doctor Name</th><th>Doctor ID</th><th>Specialization</th><th>Registration No.</th><th>Status</th><th>Actions</th></tr></thead>
    <tbody>{trs}</tbody>
  </table>
</div>
'''.format(trs=trs)
write('admin', 'verify.html', page('admin','verify.html','Doctor Verification','Approve or reject new doctor accounts.', content))

# ---------------------------------------------------------------- patients
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Patients</h1><p>Platform-wide patient accounts.</p></div></div>
<div class="card" style="padding:16px 20px;margin-bottom:16px;"><input class="input" placeholder="Search by name or patient ID..."></div>
<div class="card table-wrap">
  <table class="data-table">
    <thead><tr><th>Patient</th><th>Patient ID</th><th>Family Members</th><th>Records</th><th>Joined</th></tr></thead>
    <tbody>
      <tr><td>Amit Sharma</td><td class="text-sm">PAT-2026-000123</td><td>4</td><td>14</td><td>Jan 2026</td></tr>
      <tr><td>Priya Patil</td><td class="text-sm">PAT-2026-000456</td><td>2</td><td>6</td><td>Mar 2026</td></tr>
      <tr><td>Rakesh Jain</td><td class="text-sm">PAT-2025-000789</td><td>1</td><td>3</td><td>Nov 2025</td></tr>
    </tbody>
  </table>
</div>
'''
write('admin', 'patients.html', page('admin','patients.html','Patients','All registered patient accounts.', content))

# ---------------------------------------------------------------- access sessions
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Access Sessions</h1><p>Every active and past temporary access grant, platform-wide.</p></div></div>
<div class="card table-wrap">
  <table class="data-table">
    <thead><tr><th>Doctor</th><th>Patient</th><th>Records Shared</th><th>Duration</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Dr. Rahul Sharma</td><td>Amit Sharma</td><td>Blood Reports, Prescriptions</td><td>1 Hour</td><td><span class="badge badge-active">Active</span></td></tr>
      <tr><td>Dr. Arvind Menon</td><td>Rajesh Sharma</td><td>Previous Diagnosis</td><td>2 Hours</td><td><span class="badge badge-active">Active</span></td></tr>
      <tr><td>Dr. Neha Kulkarni</td><td>Sunita Sharma</td><td>Prescriptions</td><td>30 Minutes</td><td><span class="badge badge-notauth">Expired</span></td></tr>
    </tbody>
  </table>
</div>
'''
write('admin', 'access.html', page('admin','access.html','Access Sessions','Monitor every temporary access grant.', content))

# ---------------------------------------------------------------- analytics
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Analytics</h1><p>Platform usage over the last 30 days.</p></div></div>
<div class="grid-2">
  <div class="card" style="padding:24px;">
    <h3>Appointments per Week</h3>
    <div style="margin-top:20px;">
      <div class="mini-row"><span class="text-sm text-soft">Week 1</span><div class="mini-bar"><div style="width:62%"></div></div><span class="text-sm">742</span></div>
      <div class="mini-row"><span class="text-sm text-soft">Week 2</span><div class="mini-bar"><div style="width:74%"></div></div><span class="text-sm">890</span></div>
      <div class="mini-row"><span class="text-sm text-soft">Week 3</span><div class="mini-bar"><div style="width:58%"></div></div><span class="text-sm">701</span></div>
      <div class="mini-row"><span class="text-sm text-soft">Week 4</span><div class="mini-bar"><div style="width:81%"></div></div><span class="text-sm">871</span></div>
    </div>
  </div>
  <div class="card" style="padding:24px;">
    <h3>Access Requests</h3>
    <div style="margin-top:20px;">
      <div class="mini-row"><span class="text-sm text-soft">Approved</span><div class="mini-bar"><div style="width:78%"></div></div><span class="text-sm">78%</span></div>
      <div class="mini-row"><span class="text-sm text-soft">Rejected</span><div class="mini-bar"><div style="width:12%"></div></div><span class="text-sm">12%</span></div>
      <div class="mini-row"><span class="text-sm text-soft">Expired unused</span><div class="mini-bar"><div style="width:10%"></div></div><span class="text-sm">10%</span></div>
    </div>
  </div>
</div>
'''
write('admin', 'analytics.html', page('admin','analytics.html','Analytics','Platform usage at a glance.', content))

# ---------------------------------------------------------------- settings
content = '''
<div class="section-head"><div><h1 style="font-size:1.9rem;">Settings</h1><p>Admin console preferences.</p></div></div>
<div class="grid-2">
  <div class="card" style="padding:22px;">
    <h3>Admin Profile</h3>
    <div class="field"><label>Name</label><input class="input" value="Admin Console"></div>
    <div class="field mb-0"><label>Email</label><input class="input" value="admin@hdims.in"></div>
    <button class="btn btn-primary btn-sm" style="margin-top:16px;">Save Changes</button>
  </div>
  <div class="card" style="padding:22px;">
    <h3>Preferences</h3>
    <div class="flex justify-between items-center" style="padding:10px 0;"><span class="text-sm">Appearance</span>
      <button class="toggle-pill" data-theme-toggle><span class="t-label">Light</span></button></div>
  </div>
</div>
'''
write('admin', 'settings.html', page('admin','settings.html','Settings','Console preferences.', content))

print('admin pages done')
