The Bifurcation of Global Automotive Value Chains: Analyzing the Intersection of Cybersecurity, Clean Energy Protectionism, and Data Sovereignty (2025–2026)
The Geopolitical Fragmentation of Automotive Regimes
The global automotive sector is undergoing a structural realignment as the era of standardized, globally optimized vehicle platforms is replaced by regionalized compliance regimes [cite: 1]. Historically, automotive original equipment manufacturers (OEMs) structured supply chains around just-in-time logistics and centralized production hubs to maximize economies of scale. In the 2025–2026 regulatory environment, however, this model is no longer viable.
OEMs now operate within a highly fragmented regulatory landscape defined by national security protections, digital sovereignty mandates, and carbon border adjustments [cite: 1, 2, 3, 4]. The United States has established defensive trade barriers to exclude Chinese and Russian hardware, software, and capital from its domestic market [cite: 1, 5, 6, 7]. Simultaneously, the European Union is enforcing strict data access rights and expanding its carbon accounting mechanisms to include downstream manufactured components [cite: 2, 3, 8].
These parallel regulatory pressures are forcing global automotive manufacturers to bifurcate their product architectures, implement rigorous supply chain mapping, and pioneer new joint-venture structures to maintain access to critical Western markets [cite: 1, 9, 10, 11].
--------------------------------------------------------------------------------
The U.S. Connected Vehicle Rule: National Security and Supply Chain Isolation
To protect critical infrastructure, the U.S. Department of Commerce’s Bureau of Industry and Security (BIS) implemented a final rule under 15 C.F.R. Part 791 Subpart D, titled Securing the Information and Communications Technology and Services Supply Chain: Connected Vehicles [cite: 1, 5, 12]. Effective March 17, 2025, this regulation restricts the import, sale, and integration of connected vehicle technologies designed, developed, manufactured, or supplied by entities with a nexus to foreign adversaries—specifically the People's Republic of China (PRC) and the Russian Federation [cite: 1, 5, 12, 13].
The regulatory framework is built on the assessment that modern vehicles, equipped with persistent cellular connectivity and automated driving stacks, are vulnerable to remote cyber-exploitation, state-sponsored data harvesting, and potential kinetic manipulation by foreign state actors [cite: 5].
Connected Vehicle Regulatory Realignment (U.S. Market)
                       ┌──────────────────────────────┐
                       │  VCS Hardware / Soft Nexus   │
                       └──────────────┬───────────────┘
                                      ▼
                      Are components designed, developed, 
                      assembled, or supplied by PRC/Russia?
                                 /          \
                               Yes           No
                               /              \
         ┌──────────────────────────┐    ┌──────────────────────────┐
         │ Prohibited for U.S. Sale │    │ Annual DoC Submission    │
         │ (Unless GA Exempted)     │    │ (60 Days Prior to Sale)  │
         └──────────────────────────┘    └──────────────────────────┘
The BIS Connected Vehicle Rule defines a "connected vehicle" as any vehicle driven or drawn by mechanical power manufactured primarily for use on public streets, roads, and highways that integrates onboard networked hardware with automotive software systems to communicate via cellular, dedicated short-range, satellite, or other wireless protocols [cite: 12]. The rule excludes rail-operated vehicles and commercial vehicles with a Gross Vehicle Weight Rating (GVWR) of more than 10,000 pounds, focusing its initial enforcement on the passenger vehicle market [cite: 12].
However, U.S. lawmakers are actively working to expand this regulatory perimeter [cite: 1]. Bipartisan sponsors introduced the Connected Vehicle Security Act of 2026 (S. 4429 / H.R. 8730) alongside the Connected Vehicle National Security Review Act (S. 2040) [cite: 1, 13]. This proposed legislation seeks to eliminate the 10,000-pound GVWR exclusion, bringing heavy commercial trucks, buses, and utility fleets under the scope of the connectivity bans [cite: 1, 13].
The BIS rule focuses on two critical systems: Vehicle Connectivity Systems (VCS) and Automated Driving Systems (ADS) [cite: 1, 13]. To enforce compliance, the BIS established a tiered implementation schedule to allow manufacturers to re-engineer their supply chains [cite: 5].
U.S. Connected Vehicle Compliance Schedule and Product Classifications
System Class
Component and Technology Coverage [cite: 1, 12, 13]
Statutory Exclusions [cite: 1, 12]
Enforcement Timeline [cite: 1, 5, 12]
Vehicle Connectivity Systems (VCS)
Telematics control units, cellular modems, Wi-Fi and Bluetooth modules, satellite communication hardware, digital signal processors (DSPs), FPGAs, and external transceivers operating over 450 MHz [cite: 1, 12, 13].
Firmware, true open-source software, GNSS-only receivers, AM/FM-only antennas, and passive components (brackets, fasteners, diodes, and transistors) [cite: 1, 12].
March 17, 2025: Immediate import ban on VCS hardware with a PRC/Russia nexus for passenger vehicles under 10,000 lbs GVWR [cite: 1, 12].
Automated Driving Systems (ADS)
Autonomous driving software stacks, object detection, classification, and decision-making modules, and advanced driver-assistance systems (ADAS) operating at Level 3 and above [cite: 1, 13].
Pure sensor technologies, including LiDAR, radar, optical video camera modules, and Ultra-Wideband (UWB) proximity sensors [cite: 1].
September 30, 2026: Prohibitions on the sale of vehicles utilizing covered software with a PRC/Russia nexus for Model Year 2027 vehicles [cite: 1, 5].
The extraterritorial reach of the BIS Connected Vehicle Rule is a major operational challenge for global automotive platforms [cite: 1]. The regulation is not restricted to vehicles assembled in China or Russia [cite: 1]. It applies to vehicles built in Europe, Mexico, or the United States if any covered software or hardware component is designed, developed, manufactured, or supplied by a covered foreign entity, or if the OEM itself is under their corporate control [cite: 1].
This provenance requirement forces global platforms to segment their electronic control architectures [cite: 1]. A vehicle platform approved for the European market can be banned in the United States if its telematics control unit or over-the-air (OTA) update governance contains a PRC software or hardware nexus [cite: 1].
To verify compliance, the BIS requires VCS hardware importers and connected vehicle manufacturers to submit an electronic Declaration of Conformity (DoC) via the Compliance Application and Reporting System (CARS) at least 60 days before the first import or sale of each model year [cite: 1, 5, 12]. OEMs must conduct due diligence to certify that their supply chains contain no PRC or Russian nexus [cite: 1, 12].
Manufacturers must compile and retain a Software Bill of Materials (SBOM) and a Hardware Bill of Materials (HBOM) for at least 10 years [cite: 1]. While these documents are not routinely submitted with the annual DoC, they must be made available to the BIS immediately upon request [cite: 1].
If any material change occurs in the supply chain—such as a software patch sourced from a restricted developer—an updated DoC must be submitted within 60 days [cite: 1]. Non-compliance or false certifications are subject to severe civil and criminal penalties, including monetary fines, jail time for willful violations, and the revocation of export privileges [cite: 1, 14].
To manage transition risks, the BIS has established several narrow relief mechanisms [cite: 5, 15]:
Legacy Software Exemption: Source code designed, developed, manufactured, or supplied before March 17, 2026, is exempt from the software ban [cite: 12, 14]. However, after this compliance date, any maintenance, patching, or updates to this legacy code must be performed entirely by non-covered entities [cite: 14].
Amended General Authorization 1 (GA1): Allows connected vehicles containing non-compliant software or VCS hardware to be temporarily imported under four narrow conditions: public road use for up to 30 days in a 12-month period solely for testing; off-road display, research, or testing; on-road display or testing under specific declarations; and temporary imports of up to one year for repairs, alterations, or sporting competitions [cite: 15].
General Authorization 3 (GA3): Establishes an Approved Supplier Registry [cite: 15]. When both the importer and the supplier are registered, VCS hardware and covered software can be imported without specific transaction-by-transaction authorizations [cite: 15].
Specific Authorizations: Granted case-by-case upon review of the applicant's mitigation strategies and risk controls [cite: 5, 15].
--------------------------------------------------------------------------------
The One Big Beautiful Bill Act (OBBBA): Restructuring U.S. Clean Energy and Battery Subsidies
The regulatory environment in the United States was further altered by the enactment of the One Big Beautiful Bill Act (OBBBA) on July 4, 2025 [cite: 16, 17, 18, 19]. While the 2022 Inflation Reduction Act (IRA) utilized clean energy tax incentives to build out domestic EV capacity, the OBBBA accelerated the sunset of consumer-facing tax credits while tightening advanced manufacturing and investment credits [cite: 6, 11, 17, 20].
U.S. EV and Energy Credit Termination Schedule (OBBBA)
├── September 30, 2025: Termination of 30D (New EV), 25E (Used EV), and 45W (Commercial EV) Credits [cite: 4, 19, 21]
├── December 31, 2025: Termination of 25C (Home Efficiency) and 25D (Residential Solar/Wind) [cite: 4, 21, 22]
├── June 30, 2026: Termination of 30C (Charging Stations) and 45L (Energy Efficient Homes) [cite: 4, 21, 22]
└── December 31, 2026: Modification to 45X Integrated Component Sales [cite: 23, 24]
Under the OBBBA, the Section 30D (New Clean Vehicle Credit), Section 25E (Used Clean Vehicle Credit), and Section 45W (Commercial Clean Vehicle Credit) were terminated for any vehicle acquired after September 30, 2025 [cite: 4, 19, 21, 24]. This pulled the expiration of these critical tax incentives forward by more than seven years [cite: 4, 25].
The U.S. Treasury and IRS defined "acquired" as the date on which a written, binding contract was executed and an initial payment (such as a down-payment or vehicle trade-in) was made [cite: 21, 25]. Vehicles acquired before the September 30, 2025 cutoff remain eligible for the credits when they are "placed in service"—defined as the date the taxpayer takes physical possession of the vehicle [cite: 21, 25].
The OBBBA also ended other clean energy incentives [cite: 4, 24]:
Section 25C & 25D: Residential clean energy and home efficiency credits terminated for installations completed after December 31, 2025 [cite: 4, 21, 22, 26].
Section 30C & 45L: The alternative fuel vehicle refueling property credit and the new energy-efficient home credit terminate for property placed in service after June 30, 2026 [cite: 4, 21, 22, 24].
Section 179D: The energy-efficient commercial buildings deduction is eliminated for projects starting construction after June 30, 2026 [cite: 4, 21, 26].
The Prohibited Foreign Entity (PFE) Framework
While consumer-facing EV credits were terminated, the OBBBA retained supply-side incentives under Section 45X (Advanced Manufacturing Production Credit) and Section 48E/45Y (Clean Electricity Investment and Production Credits) to support domestic manufacturing [cite: 4, 11, 17]. However, it subjected these remaining credits to strict Prohibited Foreign Entity (PFE) restrictions [cite: 4, 17, 27].
The PFE framework builds on the IRA's Foreign Entity of Concern (FEOC) rules, classifying restricted entities into two tiers: Specified Foreign Entities (SFEs) and Foreign-Influenced Entities (FIEs) [cite: 4, 7, 19].
An SFE is defined as any entity designated as a foreign terrorist organization, included on the Office of Foreign Assets Control's (OFAC) Specially Designated Nationals (SDN) list, identified as a Chinese military company, listed under the Uyghur Forced Labor Prevention Act (UFLPA), or classified as a "foreign controlled entity" under the jurisdiction of a covered nation (China, Russia, North Korea, or Iran) [cite: 19, 27].
An FIE is any entity over which an SFE exercises significant structural, financial, or operational influence [cite: 4, 19, 28].
Structural Criteria for Foreign-Influenced Entity (FIE) Status under the OBBBA
Structural Criterion
Operational Metric or Ownership Threshold [cite: 4, 19, 28]
Regulatory Action and Implications [cite: 4, 17, 28]
Direct Governance Control
An SFE holds the direct or indirect authority to appoint a "covered officer" (including any member of the board, CEO, COO, CFO, General Counsel, or Senior VP) [cite: 4, 19, 28].
Triggers automatic FIE classification, disqualifying the entity from claiming Sections 45X, 45Y, or 48E tax credits [cite: 4, 17, 28].
Single-Entity Equity Threshold
A single SFE holds 25% or more of the entity's outstanding voting or equity stock [cite: 4, 19, 28].
Classifies the entity as foreign-influenced, restricting its participation in domestic clean energy manufacturing incentives [cite: 4, 17, 28].
Aggregate Equity Threshold
Multiple SFEs hold, in the aggregate, 40% or more of the entity's outstanding voting or equity stock [cite: 4, 19, 28].
Prevents consortiums of Chinese or Russian investors from dividing ownership to bypass the 25% single-entity limit [cite: 19, 28].
Debt Financing Threshold
Original-issuance debt held by one or more SFEs equals or exceeds 15% of the entity's total outstanding debt [cite: 4, 19, 28].
Restricts OEMs and battery developers from using state-backed Chinese banks to fund North American facilities [cite: 17, 19, 28].
Effective Control and Licensing
Payments (dividends, royalties, fees) made to an SFE under a licensing agreement that grants the SFE control over project operations or supply chain selection [cite: 4, 28].
Prevents the use of technology licensing agreements to bypass equity limits, ensuring SFEs cannot exert operational control over subsidized projects [cite: 4, 28].
The Material Assistance Cost Ratio (MACR)
To prevent clean energy projects from indirectly benefiting PFEs through material sourcing, the OBBBA limits procurement using the Material Assistance Cost Ratio (MACR) [cite: 7, 17]. Taxpayers claiming Sections 45X, 45Y, or 48E credits must prove that their projects do not include material assistance from a PFE [cite: 16, 17, 27].
The MACR is calculated mathematically using the following formula:
MACR= 
Total Direct Material Costs
Direct Material Costs of Non-PFE Sourced Components
​
 
Under Section 45X, battery manufacturers can claim credits of up to $35 per kilowatt-hour (kWh) for cells and an additional $10 per kWh for modules, provided they meet the MACR thresholds [cite: 11]. The OBBBA provides a 0% MACR requirement for critical minerals until December 31, 2029 [cite: 7, 11, 23]. This allows battery manufacturers to use PFE-sourced minerals (e.g., Chinese-refined lithium, cobalt, and nickel) without losing credit eligibility [cite: 7, 11]. Beginning in 2030, the mineral MACR threshold steps up to 25%, eventually plateauing at 50% in 2033 [cite: 7, 23].
The OBBBA also adopts a temporary lump-sum valuation method to assess compliance [cite: 7, 11]. Rather than evaluating compliance component-by-component, manufacturers can aggregate total material values [cite: 7, 11]. This allows them to offset difficult-to-source, lower-value Chinese materials (such as synthetic graphite and manganese) by using compliant, high-value domestic materials [cite: 7, 11]. However, this flexibility will face tightening: the U.S. Treasury must issue detailed, mineral-by-mineral MACR thresholds by December 31, 2027 [cite: 7, 11].
The OBBBA includes three major safe-harbor mechanisms to protect pre-existing contracts:
Existing Licensing Agreements: Intellectual property and technology licensing agreements (such as the LRS agreement between Ford and CATL) signed before July 4, 2025, are exempt from the PFE "effective control" rules, provided they are not modified [cite: 7, 11, 20]. If these contracts are modified or extended, they immediately lose their grandfathered status [cite: 7, 29].
Pre-Existing Supply Contracts: Sourcing contracts signed before June 16, 2025, are excluded from MACR calculations, provided the battery cells are sold before January 1, 2027, or the energy storage systems are deployed before January 1, 2030 [cite: 7].
Energy Storage Construction Starts: Storage projects utilizing the Section 48E credit are exempt from MACR restrictions if construction began before December 31, 2025 [cite: 7, 11, 27]. Under IRS guidance, construction status can be established via the Physical Work Test (meaningful physical work on- or off-site) or the 5% Test (incurring at least 5% of total capital costs through binding commitments) [cite: 7].
--------------------------------------------------------------------------------
Battery Sourcing Case Study: The Ford-CATL Licensing Model
The transition from the IRA's FEOC rules to the OBBBA’s PFE framework directly impacted U.S. battery joint ventures, particularly the collaboration between Ford Motor Company and Contemporary Amperex Technology Co., Limited (CATL) [cite: 7, 11, 29].
Under the original Licensing, Royalty, and Service (LRS) model, Ford designed a facility in Marshall, Michigan, to manufacture Lithium Iron Phosphate (LFP) batteries [cite: 20, 29]. Rather than forming a traditional equity joint venture, Ford retained 100% ownership of the plant and hired CATL to license its LFP battery cell technology and provide operational assistance [cite: 7, 29]. This structure was intended to bypass the IRA's strict equity-based FEOC exclusions [cite: 7, 20].
Ford-CATL LRS Facility Structural Adjustments
                          ┌────────────────────────┐
                          │   Marshall, MI Plant   │
                          │     (LFP Batteries)    │
                          └───────────┬────────────┘
                                      ├─ Originally planned at 35GWh capacity
                                      ├─ Lowered to 20GWh designed capacity
                                      ├─ LRS contract signed before July 4, 2025
                                      └─ Grandfathered under OBBBA if unmodified
The OBBBA’s "effective control" and PFE provisions directly target these licensing arrangements [cite: 7, 17, 28]. Under the new regulations, any licensing agreement with an SFE that grants operational control or restricts supplier selection can classify the licensee as an FIE, disqualifying the project from Section 45X production credits [cite: 7, 28].
However, because Ford and CATL signed their LRS contract before the July 4, 2025 OBBBA enactment date, the agreement is grandfathered under the licensing safe harbor [cite: 7]. This allows the Marshall facility to remain eligible for the $35/kWh Section 45X production credit when it begins production in 2026, provided the contract is not modified or extended [cite: 7, 11, 29].
This grandfathering protection did not automatically extend to Ford’s other battery projects [cite: 29]. In late 2025, Ford and SK On modified their joint venture arrangements in Kentucky and Tennessee [cite: 29]. Ford took independent ownership of the twin battery plants in Glendale, Kentucky, which were originally designed to manufacture nickel-rich pouch cells [cite: 29].
Ford announced plans to convert these Kentucky facilities to manufacture LFP-based Battery Energy Storage Systems (BESS) for grid-scale applications, targeting an annual capacity of 20GWh by late 2027 [cite: 29].
To support this conversion, Ford explored expanding its LRS agreement with CATL to include BESS production [cite: 29]. However, because this represents an expansion of the licensing contract after the July 4, 2025 cutoff, the new agreement is subject to full PFE scrutiny [cite: 7, 29].
If the IRS determines that the new licensing terms grant CATL "effective control" over the Kentucky operations, the facility will lose its eligibility for both the Section 45X advanced manufacturing credit and the Section 48E investment tax credit [cite: 7, 28, 29].
This regulatory pressure is driving U.S. developers to seek alternative, non-PFE sources of LFP battery technology [cite: 20, 29].
--------------------------------------------------------------------------------
Chinese EV Localization Strategies in Europe: Case Studies
While the U.S. market has utilized cybersecurity rules and clean energy tax structures to isolate its domestic supply chains, the European Union has implemented a different mix of import tariffs and rules-of-origin standards [cite: 1, 9, 30].
To bypass these trade barriers, Chinese EV manufacturers are shifting from an export-driven model to local European production [cite: 9, 30, 31].
BYD European Industrial Footprint Shifts
                     ┌──────────────────────────────────┐
                     │   BYD Global Export Strategy     │
                     └────────────────┬─────────────────┘
                                      │
            ┌─────────────────────────┴─────────────────────────┐
            ▼                                                   ▼
┌───────────────────────┐                           ┌───────────────────────┐
│ Szeged, Hungary Plant │                           │ Manisa, Turkey Plant  │
│                       │                           │                       │
│ - Trial Prod: Jan 2026│                           │ - $1B Project Paused  │
│ - Series: Q4 2026     │                           │ - No Active Timeline  │
│ - Capacity: 200k/Year │                           │ - Tariff Exemptions   │
│ - Avoids EU Tariffs   │                           │   Under Scrutiny      │
└───────────────────────┘                           └───────────────────────┘
Case Study 1: BYD Hungary Factory (Szeged)
BYD's factory in Szeged, Hungary, represents the company's primary manufacturing hub in Europe [cite: 30, 31, 32, 33]. The facility is designed to reach an annual capacity of 200,000 vehicles, allowing BYD to manufacture electric vehicles within the EU and bypass import tariffs [cite: 30, 31, 33, 34].
Despite BYD's fast-paced construction timelines in China, the company has faced slower-than-expected progress in Europe due to local regulatory approvals and equipment installation delays [cite: 30, 31, 32]. Originally scheduled to begin series assembly by the end of 2025, BYD delayed the start of commercial production to the fourth quarter of 2026 [cite: 30, 31, 32, 34].
However, BYD reached a major milestone in late January 2026, when it officially commenced trial pilot production at the Szeged facility [cite: 33]. The plant currently employs approximately 960 local and international workers to support the tooling and production ramp-up [cite: 33].
The first model scheduled for full assembly is the BYD Dolphin Surf (a compact EV known as the Seagull in China), which will serve as the entry point for BYD’s European-built lineup [cite: 30, 31, 32, 33].
In contrast, BYD paused its planned $1 billion factory project in Manisa, Turkey [cite: 30, 31, 34]. Announced in July 2024 under an agreement with Turkey's Ministry of Industry and Technology, the plant was designed to produce 150,000 hybrid and electric vehicles annually [cite: 34].
Under this agreement, BYD was exempted from Turkey's 40% additional customs duty on Chinese vehicle imports, allowing the company to import 26,610 vehicles tariff-free between late 2025 and early 2026 while expanding its retail network to 43 dealerships [cite: 34].
However, with construction in Manisa stalled, opposition lawmakers have criticized the Turkish government for granting tariff exemptions before construction began [cite: 34]. BYD has confirmed that the Turkish project remains paused with no active timeline as the company prioritizes its Hungarian operations [cite: 30, 31, 32, 34].
Case Study 2: Stellantis and Leapmotor Alliance
Stellantis and Leapmotor have expanded their strategic relationship through the Leapmotor International (LPMI) joint venture [cite: 9, 35, 36]. LPMI is structured as a 51% Stellantis and 49% Leapmotor joint venture [cite: 9, 35].
The partnership has shifted from a distribution-focused model to one centered on shared manufacturing infrastructure and vehicle platform integration [cite: 9]. In 2025, the joint venture recorded over 40,000 vehicle shipments across Europe through 850 retail points of sale, utilizing Leapmotor's T03 and C10 models [cite: 9, 36].
Stellantis-Leapmotor European Manufacturing Hubs
├── Zaragoza Plant (Figueruelas, Spain)
│   ├── Leapmotor B10 (C-SUV) ── Production begins 2026
│   └── Electric Opel C-SUV ──── Production begins 2028 (Sourcing Chinese parts via LPMI)
└── Villaverde Plant (Madrid, Spain)
    └── Leapmotor Nameplates ── Allocation starts H1 2028 (Under evaluation for ownership transfer)
The joint venture's dual-plant manufacturing strategy in Spain leverages underutilized Stellantis capacity:
The Zaragoza Plant (Figueruelas): This facility, which has produced over 10 million Opel Corsas, currently builds the Peugeot 208 and Lancia Ypsilon [cite: 9, 36]. Stellantis is adding a new assembly line to build the Leapmotor B10 (C-SUV) starting in 2026 [cite: 9, 36]. In 2028, the plant will add an all-electric Opel C-SUV designed in Germany [cite: 9, 36]. This Opel model will integrate parts sourced directly through the LPMI joint venture, leveraging Leapmotor's cost-competitive supply chain to lower bill-of-materials costs and improve European BEV affordability [cite: 9, 36].
The Villaverde Plant (Madrid): This facility currently builds the Citroën C4, which is approaching the end of its life cycle [cite: 9]. The partners plan to allocate new Leapmotor models to the plant starting in the first half of 2028 [cite: 9, 36]. To support this, Stellantis is in discussions to transfer direct ownership of the Villaverde facility to LPMI’s Spanish subsidiary [cite: 9, 36]. This structural shift will transition the joint venture from a contract manufacturing model to one where LPMI directly controls its own European production assets [cite: 9]. All vehicles assembled at Villaverde will comply with upcoming "Made-in-Europe" rules-of-origin standards to bypass EU tariffs [cite: 9].
This cooperative model aligns with Stellantis' broader "FaSTLAne 2030" strategic plan, launched in May 2026 [cite: 35, 37]. The plan targets over €60 billion in capital allocation through 2030, focusing 70% of product investments on its core global brands (Jeep, Ram, Peugeot, FIAT) and its Pro One commercial vehicle unit [cite: 35, 37].
FaSTLAne 2030 also aims to improve European capacity utilization to 80% by reducing capacity by 800,000 units and repurposing plants without shutdowns [cite: 35]. Additionally, the plan seeks to accelerate vehicle development cycles from 44 months to 24 months, using joint ventures like LPMI to source cost-competitive EV technology [cite: 9, 35].
--------------------------------------------------------------------------------
The EU Carbon Border Adjustment Mechanism (CBAM) Downstream Expansion
As European manufacturers localize assembly, they must also navigate the EU's evolving carbon accounting framework [cite: 2, 38]. The Carbon Border Adjustment Mechanism (CBAM) entered its definitive phase on January 1, 2026, ending the transitional reporting period [cite: 2, 38, 39, 40].
Under the definitive phase, EU importers of raw commodities—specifically iron, steel, aluminum, cement, fertilizers, electricity, and hydrogen—must purchase CBAM certificates to offset the embedded carbon emissions of their imports [cite: 39, 41, 42, 43]. These certificate prices are linked directly to the weekly average auction price of the EU Emissions Trading System (ETS) [cite: 40, 42, 43].
The original CBAM framework left a structural gap [cite: 2]. Non-EU manufacturers could import CBAM-covered raw steel and aluminum, fabricate them into finished vehicle components or machinery outside the EU, and export those completed products to the EU without paying a carbon fee [cite: 2]. This circumvention incentivized companies to relocate fabrication processes outside the European Union, leading to "carbon leakage" [cite: 2, 41, 43, 44].
To address this, the European Commission proposed an expansion of CBAM on December 17, 2025, targeting approximately 180 downstream steel- and aluminum-intensive products [cite: 2, 10, 39, 44]. On June 12, 2026, the EU Council agreed on its general position to advance this downstream expansion through the legislative process [cite: 10, 39, 40].
The downstream expansion is expected to bring approximately 7,500 new importers into the CBAM compliance system [cite: 2, 10]. It will apply a carbon price to an additional 2.5% of total EU imports, on top of the 4.7% covered during the upstream definitive phase [cite: 38].
Importers must register as Authorized CBAM Declarants and purchase certificates to cover the embedded emissions of their products [cite: 10, 39, 42]. Unlike the upstream phase, which measures direct emissions from raw production, the downstream mechanism measures emissions based solely on the raw steel or aluminum precursors [cite: 10]. The energy consumed during downstream fabrication or assembly is excluded from the calculation [cite: 10].
Importers must calculate emissions at the installation level (production plant) rather than using company-wide averages [cite: 10, 44]. If an importer cannot secure verified emissions data from a supplier, the EU will apply default values based on the highest-emitting installations in the exporting country, which increases the carbon tax liability [cite: 40, 42, 43].
If a carbon price has already been paid in the country of origin, that fee can be deducted from the required CBAM certificates [cite: 42, 43]. However, countries without carbon pricing mechanisms face significant trade costs [cite: 42, 45]. For example, studies suggest that applying CBAM to the entire automotive supply chain could act as an ad valorem tariff of up to 4.6% on Chinese automotive exports by 2034, and up to 2.6% for South Korea and Japan [cite: 38].
EU Council Position (June 12, 2026) ─────────────────┐
                                                    ├─► Downstream Scope Finalization
Environment Committee Position (ENVI, Sep 2026) ────┘  * Target: 180+ codes (79% metal)
                                                       * Closes online sales loophole
                                                       * Introduces anti-circumvention tools
                                                       * TDF Funding: €630M (2028-2029)
The European Parliament's Environment Committee (ENVI) adopted a position in September 2026 that supports the Commission's proposal while adding several strict anti-circumvention measures [cite: 10, 40]:
Online Sales Loophole: Introduces rules to apply CBAM requirements to direct-to-consumer online imports [cite: 40].
True Country of Origin: Empowers the Commission to apply default emissions values from the true country of origin if a pattern of transshipment or circumvention is detected [cite: 40].
Temporary Decarbonisation Fund (TDF): Proposed to operate from 2028 to 2029 with a value of up to €630 million [cite: 40, 46]. The TDF will allocate 25% of CBAM revenues to temporarily support EU manufacturers in sectors facing high carbon leakage risks (fertilizers, aluminum, iron, and steel) as ETS free allowances are phased out [cite: 40, 46].
This expanded CBAM framework positions the EU as the most ambitious jurisdiction globally for carbon border adjustments, contrasting with the UK's upstream-only model and Australia's cement-focused proposals [cite: 38].
--------------------------------------------------------------------------------
The Dual Regulatory Layer in Europe: GDPR and the EU Data Act for Connected Vehicles
As European automotive supply chains navigate carbon tariffs, their digital systems must comply with a complex dual regulatory framework: the General Data Protection Regulation (GDPR) and the EU Data Act [cite: 3, 8, 47]. Effective since September 2025, the EU Data Act (Regulation (EU) 2023/2854) established a horizontal framework that treats vehicle-generated telemetry as accessible, portable data [cite: 3, 8, 47].
EU Connected Vehicle Digital Framework (September 2025 Onward)
                       ┌──────────────────────────────┐
                       │     Connected Vehicle        │
                       └──────────────┬───────────────┘
                                      │ Telemetry (Raw & Pre-processed)
                                      ▼
                       ┌──────────────────────────────┐
                       │      OEM Backend Cloud       │
                       └──────────────┬───────────────┘
                                      │
            ┌─────────────────────────┴─────────────────────────┐
            ▼                                                   ▼
┌───────────────────────┐                           ┌───────────────────────┐
│     EU Data Act       │                           │      EU GDPR          │
│                       │                           │                       │
│ - Machine-readable    │                           │ - Article 15: Access  │
│ - No undue delay      │                           │ - Article 20: Port    │
│ - Non-discriminatory  │                           │ - Valid Legal Basis   │
│ - Trade Secrets Safe  │                           │ - ePrivacy Consent    │
└───────────────────────┘                           └───────────────────────┘
The Data Act grants vehicle holders and lessees the right to access all raw and pre-processed data generated by their vehicles [cite: 3, 8, 48]. The vehicle manufacturer (the data holder) must make this data available securely, without undue delay, free of charge, and in a commonly used, machine-readable format (such as ISO ExVe or COVESA VSS APIs) [cite: 3, 8, 48].
The regulation excludes highly processed, inferred, or derived data created through proprietary algorithms, protecting the OEM’s core intellectual property [cite: 48, 49]. Users can also require the OEM to stream this data directly to third-party service providers, such as independent repair shops, insurance providers, or fleet management platforms [cite: 3, 8, 48].
The Data Act does not override the GDPR (Regulation (EU) 2016/679); the two frameworks coexist [cite: 3, 47, 48]. This dual layer creates significant operational challenges for OEMs and fleet operators:
The Personal Data Status of Telemetry: Vehicle telemetry, such as GPS location history or driving style, is classified as personal data under the GDPR because it can be linked back to an identifiable driver [cite: 8, 47]. Under the GDPR, this data can only be processed if there is a valid legal basis or if explicit consent has been secured [cite: 8, 47].
The Shared-User Validation Challenge: In shared vehicle scenarios (such as rental fleets or corporate pools), multiple drivers generate data within the same vehicle [cite: 47, 50, 51]. Sharing a comprehensive telemetry history with the vehicle owner or a third party can violate the privacy rights of previous drivers [cite: 3, 51]. Legal analyses recommend relying on the "primary user" (the registered owner or lessee) when validating data access requests to manage these privacy risks [cite: 51].
Data Minimization vs. Data Access Barriers: GDPR principles mandate that companies minimize the collection and storage of personal data [cite: 50]. However, if an OEM deliberately restricts telemetry collection to avoid Data Act obligations, it faces regulatory scrutiny [cite: 51]. The European Commission has warned that OEMs cannot use "data minimization as an access barrier" to avoid compliance [cite: 51].
Disputes Over Offline Data: There is ongoing debate regarding data that is stored locally on the vehicle and can only be extracted physically via the On-Board Diagnostics (OBD II) port [cite: 8, 51]. While some operators argue this offline data falls outside the scope of "continuous telemetry," consumer groups argue that all technically retrievable data must be portable under the Act [cite: 48, 51].
--------------------------------------------------------------------------------
Synthesis of Geopolitical Regimes: The Segmented Global OEM
The divergence between U.S. national security regulations and EU environmental and digital frameworks is driving a permanent structural division in the automotive sector [cite: 1, 2, 4, 38]. Rather than utilizing a unified global platform, OEMs must now design and operate parallel, regionalized architectures [cite: 1].
Functional Realignment of Global OEM Architectures
                  ┌──────────────────────────────────────┐
                  │  Standardized Platform Prototyping   │
                  └──────────────────┬───────────────────┘
                                     │
            ┌────────────────────────┴────────────────────────┐
            ▼                                                 ▼
┌─────────────────────────────────────┐   ┌─────────────────────────────────────┐
│       U.S. Compliant Architecture   │   │        E.U. Compliant Architecture  │
│                                     │   │                                     │
│ - Decoupled Software & VCS          │   │ - Data Act-Ready Telemetry APIs     │
│   (No PRC/Russia Nexus) [cite: 1]   │   │   (Open API, Machine-Readable) [cite: 48]│
│ - Non-PFE Sourced Components        │   │ - CBAM Carbon-Tracked Precursors    │
│   (Strict MACR Sourcing) [cite: 17]   │   │   (Verified Plant Emissions) [cite: 10] │
│ - Domestic Battery Sourcing         │   │ - "Made-in-Europe" Rules of Origin  │
│   (Section 45X AMPC Compliant) [cite: 11]│   │   (Tariff Avoidance Local Assembly) [cite: 9]│
└─────────────────────────────────────┘   └─────────────────────────────────────┘
The U.S. market is defined by national security exclusions that restrict software provenance, supply chain connections to foreign adversaries, and international technology licensing [cite: 1, 17]. Conversely, the European market is defined by carbon border taxes and open, user-centric data sovereignty [cite: 2, 8].
To remain competitive, global automotive companies must separate their development processes, implement rigorous supply chain tracking, and establish parallel architectures that comply with the distinct regulatory requirements of each region [cite: 1, 8, 11, 42].