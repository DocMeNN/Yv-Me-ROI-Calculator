# Yv-Me ROI Calculator - V2.1 Project Schedule & Progress

## CURRENT CHECKPOINT

Branch: v2.1-dev
Remote: origin/v2.1-dev
V2.0: FROZEN / TAGGED v2.0.0
V2.1: ACTIVE DEVELOPMENT

## OVERALL PROGRESS

V1 Foundation                    100%
V2.0 Investor Intelligence      100%
V2.1 Development                  0%

Overall project maturity:        75%

## V2.1 DEVELOPMENT SCHEDULE

| Phase | Workstream | Status | Progress |
|---|---|---|---:|
| 1 | Unified Assumptions Layer | NOT STARTED | 0% |
| 2 | Executive Decision Layer | NOT STARTED | 0% |
| 3 | Scenario Dashboard 2.1 | FOUNDATION COMPLETE | 50% |
| 4 | Sensitivity Dashboard 2.1 | ENGINE COMPLETE | 50% |
| 5 | Cash Flow & Returns Intelligence | ENGINE COMPLETE | 50% |
| 6 | Partnership Intelligence 2.1 | ENGINE COMPLETE | 50% |
| 7 | Funding Strategy Intelligence | ENGINE COMPLETE | 50% |
| 8 | Executive Dashboard 2.1 | FOUNDATION COMPLETE | 50% |
| 9 | Export 2.1 | NOT STARTED | 0% |
| 10 | Acceptance, Regression & Freeze | NOT STARTED | 0% |

## WHAT IS ALREADY BUILT

### V1 FOUNDATION
- Adjustable programme assumptions
- 1 CHEW : 10 beneficiaries model
- Revenue calculation
- Programme cost calculation
- ROI
- Break-even
- Scaling analysis
- Revenue/cost analysis
- Investor/partner view
- Financial intelligence
- Grant/donor intelligence
- Sustainability intelligence
- Investor intelligence
- Excel export
- PowerPoint export

### V2.0
- Five-year cash flow engine
- Investor cash flow engine
- Investor returns
- NPV
- IRR
- Four scenario projection engine
- Partnership structures
- Funding mix
- Sensitivity engine
- Investment case engine
- KPI engine
- V2 dashboard
- Command centre
- Navigation
- Streamlit integration
- Automated tests
- V2.0 export integration

## CURRENT V2.1 ARCHITECTURE

V1 PROGRAMME MODEL
        |
        v
UNIFIED V2.1 ASSUMPTIONS
        |
        +--> V1 FINANCIAL CALCULATOR
        |
        +--> V2 INVESTMENT CASE
        |
        +--> V2 SCENARIOS
        |
        +--> V2 PARTNERSHIP
        |
        +--> V2 CASH FLOW
        |
        +--> V2 SENSITIVITY
        |
        +--> V2 FUNDING MIX
        |
        v
EXECUTIVE INTELLIGENCE
        |
        v
UNIFIED DASHBOARD
        |
        v
EXCEL / PPTX EXPORTS

## NEXT BUILD ORDER

1. Build unified assumptions state.
2. Connect V1 programme calculator to unified assumptions.
3. Connect all V2 modules to unified assumptions.
4. Remove duplicated/hard-coded V2 assumptions.
5. Bring V1 financial intelligence into the V2 shell.
6. Build executive decision engine.
7. Upgrade scenario/sensitivity/cash-flow/partnership/funding views.
8. Build final executive command centre.
9. Connect V2.1 exports.
10. Run complete regression.
11. Freeze and tag V2.1.0.

## CURRENT IMMEDIATE PRIORITY

PHASE 1 - UNIFIED ASSUMPTIONS LAYER

The objective is to establish one authoritative assumption state that drives
the entire application.

Required core assumptions:

- CHEWs
- Beneficiaries per CHEW
- Total beneficiaries
- Programme duration
- Monthly subscription
- Collection rate
- Programme/operating cost
- Setup cost
- Initial investment
- Partner revenue share
- Grant funding
- Projection period
- Discount rate
- Scenario
- Partnership structure

No dashboard module should maintain an independent copy of these assumptions.

## ACCEPTANCE TARGET

At V2.1 freeze:

V1 + V2 functionality must operate through one coherent Streamlit
application launched from the project root with:

    streamlit run app.py

All financial modules must consume the same authoritative assumptions.

V2.1 must preserve the validated V1 financial model while adding the
investor, partnership, scenario, sensitivity, cash-flow, funding and
executive intelligence capabilities of V2.

## CURRENT STATUS

V1 = COMPLETE
V2.0 = COMPLETE
V2.1 = ACTIVE

Immediate build:
UNIFIED ASSUMPTIONS LAYER
