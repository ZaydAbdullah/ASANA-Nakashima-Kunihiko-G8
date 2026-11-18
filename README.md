# ASANA: Public Transport Route and Stop Locator
### Phase 1 — Account Feature

**Student:** Kunihiko J. Nakashima  
**Section:** CSIT327 — G8  
**Repository:** ASANA-Nakashima-Kunihiko-G8

---

## Overview

ASANA is a public transport route and stop locator system. This repository contains **Phase 1**: the **Account Feature**, which is the foundation for all future phases.

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.1 (Python) |
| Frontend | Django Templates + Bootstrap 5 + Bootstrap Icons |
| Database | PostgreSQL (Supabase) |
| Auth | Django's built-in authentication (PBKDF2 hashed passwords) |

## Phase 1 Deliverables

### ✅ Account Registration
- Username, email, role, password + confirmation
- Server-side validation (required fields, unique username/email, valid email format, matching passwords)
- Passwords hashed via Django's PBKDF2 (never stored plaintext)
- Success/error messages via Django messages framework

### ✅ Login / Logout
- Login with credentials; clear error on invalid attempt
- Logout via **POST** (modern Django security best practice)
- Protected pages use `@login_required`
- Logged-out users redirected to login with `?next=` preserved

### ✅ Role-Based User Dashboards
- Two roles: `COMMUTER` and `ADMIN`
- After login, each user redirected to their role's dashboard
- Cross-role access blocked with redirect + error message
- Separate content and navigation per role

### ✅ User Profile
- Users can view and update: first name, last name, email, contact number, profile photo
- Users can only edit their **own** profile (uses `request.user`, not URL parameter)
- Password change flow included

## Phase 2 (Planned)

SDD features to be built on top of this auth foundation:
- Routes & Stops directory
- Timetables
- Interactive map (polyline overlays, stop markers)
- Search & auto-complete
- Nearby stop locator (GPS proximity)
- Favorites (max 10 per user)
- Delay reports (crowdsourced)
- Admin CRUD for transit data

## Setup Instructions

### 1. Clone and install

```bash
git clone https://github.com/YOURUSERNAME/ASANA-Nakashima-Kunihiko-G8.git
cd ASANA-Nakashima-Kunihiko-G8
python -m venv venv
venv\Scripts\activate         # Windows
# source venv/bin/activate    # Mac/Linux
pip install -r requirements.txt


---

## Author

**Kunihiko J. Nakashima**  
BSIT 3 — CSIT327 G8  
ASANA: Public Transport Route and Stop Locator