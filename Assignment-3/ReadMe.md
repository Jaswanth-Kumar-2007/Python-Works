# ✅ Phone Simulation System — GitHub Checklist

## 🧩 Object-Oriented Focus

- [ ] Define `Phone` class
- [ ] Include attributes: phone number, owner name, contacts, call history, call status
- [ ] Implement methods: place call, receive call, end call, show status
- [ ] Manage phone states: calling, receiving, in call, idle
- [ ] Maintain shared directory for all phone objects

---

## 📇 Contact Management (CRUD)

- [ ] Add contact (prevent duplicates)
- [ ] Retrieve contact by number
- [ ] Update contact name
- [ ] Delete contact by number
- [ ] Handle invalid cases with proper messages

---

## 🔍 Search Functionalities

- [ ] Search by number
- [ ] Search by name (case-insensitive)
- [ ] Keyword-based search (multi-token, order-independent)

---

## ☎️ Call Simulation

- [ ] Restrict to one active call per phone
- [ ] Show “Device is busy” if either side is in call
- [ ] Display correct messages:
  - [ ] “Calling name...”
  - [ ] “Incoming call from name (number)”
  - [ ] “In call with name...”
  - [ ] “No active call”
- [ ] Update both phones’ statuses correctly

---

## 🧾 Call History

- [ ] Maintain consistent call record structure
- [ ] Record type: dialled, received, missed
- [ ] Store start time, end time, duration
- [ ] Update both phones after every call event
- [ ] Handle rejected or missed calls

---

## 📂 File-Based Simulation

- [ ] Read actions from input file
- [ ] Parse commands:
  - [ ] `CREATE PHONE <owner name> <phone number>`
  - [ ] `ADD CONTACT <owner number> <contact name> <contact number>`
  - [ ] `CALL <caller number> <receiver number> <timestamp>`
  - [ ] `ACCEPT <receiver number> <timestamp>`
  - [ ] `END <phone number> <timestamp>`
- [ ] Execute each command sequentially
- [ ] Validate all numbers exist before actions

---

## 📊 Statistical Analysis

- [ ] Calculate total unique numbers called
- [ ] Calculate average call duration
- [ ] Identify most frequently called number(s)
- [ ] Display per-phone statistics summary

---

## 🧮 Data Types

- [ ] Strings for phone number and name
- [ ] Dictionary for contacts
- [ ] List for call history
- [ ] Boolean flags for states
- [ ] Integer/float for timestamps

---

## 💬 Status Messages

- [ ] Outgoing call message
- [ ] Incoming call message
- [ ] Active call message
- [ ] Idle status message

---

## 🧰 Error Handling

- [ ] Reject invalid phone creation
- [ ] Prevent duplicate contacts
- [ ] Handle unknown numbers gracefully
- [ ] Prevent simultaneous calls
- [ ] Handle invalid commands from file

---

## 📦 Submission & Documentation

- [ ] Include all `.py` files
- [ ] Include `README.md` with instructions
- [ ] Add screenshots of sample runs
- [ ] Show placing, accepting, and ending a call
- [ ] Show at least one search example
- [ ] Show statistical analysis output
- [ ] Code is readable, commented, and uses only Python standard library

---

## 🧱 Bonus (Optional Enhancements)

- [ ] Implement missed call detection
- [ ] Add timestamp formatting
- [ ] Support call rejection and busy tone
- [ ] Display contact name in call logs
- [ ] Generate report file of call statistics
- [ ] Add menu-driven CLI for manual testing

---

## ✅ Final Checks Before Submission

- [ ] All classes implemented and tested
- [ ] All functions working as expected
- [ ] All required outputs printed clearly
- [ ] Sample input file tested successfully
- [ ] Statistics verified for correctness
- [ ] Project folder organized and clean
- [ ] Submitted before deadline

---
