# Yv-Me ROI Calculator — V2 PROJECT SCHEDULE

**Version:** V2  
**Branch:** `v2.0-dev`  
**Current Milestone:** Engine Layer Complete  
**Status Date:** 2026-08-21

---

# V2 DEVELOPMENT ROADMAP

## PHASE 1 — V2 FINANCIAL ENGINE FOUNDATION

**Status: ✅ COMPLETE**

| Workstream | Status |
|---|---|
| Five-year cash flow foundation | ✅ |
| Investor return engine foundation | ✅ |
| Investor return scenarios | ✅ |
| Four-scenario projection engine | ✅ |
| NPV engine | ✅ |
| IRR engine | ✅ |

**Exit criterion:** Core financial calculation capability operational and tested.

---

# PHASE 2 — PARTNERSHIP & CAPITAL STRUCTURE

**Status: ✅ COMPLETE**

| Workstream | Status |
|---|---|
| Partnership structure catalogue | ✅ |
| Revenue share model | ✅ |
| Grant model | ✅ |
| Equity model | ✅ |
| Blended finance model | ✅ |
| Programme sponsorship model | ✅ |
| Working capital model | ✅ |
| Funding mix engine | ✅ |
| Funding gap detection | ✅ |
| Funding surplus detection | ✅ |

**Exit criterion:** Multiple investment/funding structures can be evaluated programmatically.

---

# PHASE 3 — INVESTMENT ANALYSIS

**Status: ✅ COMPLETE**

| Workstream | Status |
|---|---|
| Sensitivity engine | ✅ |
| Subscription sensitivity | ✅ |
| Beneficiary sensitivity | ✅ |
| Collection-rate sensitivity | ✅ |
| Operating-cost sensitivity | ✅ |
| Investment case integration | ✅ |
| Programme cash flows | ✅ |
| Investor cash flows | ✅ |
| Investor NPV | ✅ |
| Investor IRR | ✅ |
| Investor ROI | ✅ |
| Payback | ✅ |

**Exit criterion:** A complete investment case can be generated from one integrated engine.

---

# PHASE 4 — KPI & DECISION INTELLIGENCE

**Status: 🟢 ENGINE COMPLETE / UI PENDING**

| Workstream | Status |
|---|---|
| KPI calculation engine | ✅ |
| Beneficiary KPI | ✅ |
| Collection-rate KPI | ✅ |
| Revenue KPI | ✅ |
| Operating-cost KPI | ✅ |
| Operating-margin KPI | ✅ |
| ROI KPI | ✅ |
| Revenue/beneficiary KPI | ✅ |
| Cost/beneficiary KPI | ✅ |
| KPI dashboard presentation | ⏳ |

**Exit criterion:** Decision-makers can understand the financial and operating performance without reading raw calculations.

---

# PHASE 5 — V2 INVESTMENT DASHBOARD

**Status: ⏳ NEXT**

### 5.1 Assumptions Interface
- [ ] Beneficiary assumptions
- [ ] Subscription assumptions
- [ ] Collection rate
- [ ] Operating cost
- [ ] Setup cost
- [ ] Investment amount
- [ ] Revenue share
- [ ] Equity percentage
- [ ] Projection period
- [ ] Discount rate

### 5.2 Partnership Interface
- [ ] Select partnership structure
- [ ] Display partner investment
- [ ] Display partner revenue share
- [ ] Display equity exposure
- [ ] Compare structures

### 5.3 Funding Mix Interface
- [ ] Add funding source
- [ ] Define funding amount
- [ ] Define funding type
- [ ] Revenue share input
- [ ] Equity input
- [ ] Funding gap indicator
- [ ] Funding surplus indicator

### 5.4 Investment Returns
- [ ] Investor ROI
- [ ] Payback
- [ ] NPV
- [ ] IRR
- [ ] Annual investor cash flows

### 5.5 Sensitivity Dashboard
- [ ] Subscription sensitivity
- [ ] Beneficiary sensitivity
- [ ] Collection-rate sensitivity
- [ ] Operating-cost sensitivity
- [ ] Visual comparison

### 5.6 KPI Dashboard
- [ ] KPI cards
- [ ] Financial indicators
- [ ] Operating indicators
- [ ] Investor indicators

**Exit criterion:** User can enter assumptions and obtain a complete investment decision view without editing Python code.

---

# PHASE 6 — INVESTMENT DECISION VIEW

**Status: ⏳ PLANNED**

Build a high-level decision layer showing:

- Base case
- Upside case
- Downside case
- Investor return
- Programme return
- Funding requirement
- Funding structure
- Key risks
- Sensitivity exposure
- Critical assumptions
- Decision recommendation

**Exit criterion:** A private investor, donor or strategic partner can understand the investment case from one screen.

---

# PHASE 7 — EXPORT & REPORTING

**Status: ⏳ PLANNED**

### Excel
- [ ] Investment assumptions
- [ ] Projection
- [ ] Partnership comparison
- [ ] Funding mix
- [ ] Sensitivity
- [ ] KPIs
- [ ] Investor returns

### PowerPoint
- [ ] Executive investment summary
- [ ] Financial model
- [ ] Partnership options
- [ ] Funding structure
- [ ] Investor returns
- [ ] Sensitivity
- [ ] Recommendation

### PDF / Report
- [ ] Investment case summary
- [ ] Assumptions
- [ ] Financial projections
- [ ] Returns
- [ ] Risk/sensitivity

**Exit criterion:** V2 outputs can be used directly in investment and partnership discussions.

---

# PHASE 8 — VALIDATION & RELEASE CANDIDATE

**Status: ⏳ PLANNED**

- [ ] Full regression test
- [ ] Dashboard test
- [ ] Export test
- [ ] Edge-case testing
- [ ] Zero-value testing
- [ ] Large-scale scenario testing
- [ ] UI consistency review
- [ ] Financial logic review
- [ ] Documentation review
- [ ] Git status clean
- [ ] Release candidate tag

---

# PHASE 9 — V2 FINAL RELEASE

**Status: ⏳ PLANNED**

Release requirements:

- [ ] All tests passing
- [ ] Dashboard functional
- [ ] Exports functional
- [ ] Documentation complete
- [ ] LIVE_STATUS updated
- [ ] PROJECT_SCHEDULE updated
- [ ] Changelog updated
- [ ] Release tag created
- [ ] Remote synchronized

Target release:

`v2.0.0`

---

# OVERALL V2 PROGRESS

| Phase | Status |
|---|---|
| Phase 1 — Financial Engine Foundation | ✅ Complete |
| Phase 2 — Partnership & Capital Structure | ✅ Complete |
| Phase 3 — Investment Analysis | ✅ Complete |
| Phase 4 — KPI & Decision Intelligence | 🟢 Engine Complete |
| Phase 5 — Investment Dashboard | ⏳ Next |
| Phase 6 — Investment Decision View | ⏳ |
| Phase 7 — Export & Reporting | ⏳ |
| Phase 8 — Validation & RC | ⏳ |
| Phase 9 — V2 Release | ⏳ |

---

# GOVERNANCE

Every completed phase must have:

- Code committed
- Tests passing
- Remote branch synchronized
- Status updated
- Schedule updated
- Appropriate Git tag where a major milestone is reached

No major phase should be started without confirming the previous phase is stable.
