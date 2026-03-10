# Strategic Roadmap for Securing Hybrid Hardware Architecture and Physical Design Roles at NVIDIA

## The 2026 Semiconductor Landscape and the Rise of Extreme Codesign

The global semiconductor industry is navigating a profound structural paradigm shift, irrevocably altered by the insatiable computational demands of artificial intelligence, large language models (LLMs), and highly parameterized mixture-of-experts (MoE) architectures.1 For decades, the industry relied on the predictable scaling laws of Moore's Law and Dennard Scaling, wherein shrinking transistor geometries naturally yielded faster, more power-efficient monolithic chips.3 That era has definitively concluded. The physical limitations of atomic-scale manufacturing, coupled with the exponential growth in the parameter counts of deep neural networks, have necessitated an evolutionary leap in how hardware is conceived, architected, and physically realized.4

In this new epoch, the fundamental unit of compute is no longer the isolated processor on a printed circuit board; rather, the data center rack itself has become the macro-chip.2 NVIDIA sits at the absolute vanguard of this transition, pioneering an engineering philosophy termed "extreme codesign".7 Extreme codesign dictates that graphics processing units (GPUs), central processing units (CPUs), memory fabrics, high-speed networking, power delivery systems, and liquid cooling mechanisms can no longer be optimized in isolation.6 They must be architected simultaneously as a single, interdependent super-system.6 This holistic approach ensures that architectural intent is not subsequently bottlenecked by physical packaging limitations, signal integrity degradation, or thermal throttling.

The manifestation of this philosophy is the NVIDIA Vera Rubin platform, which has redefined the boundaries of high-performance computing in 2026.2 Systems like the Vera Rubin NVL72 integrate 72 Rubin GPUs and 36 Vera CPUs, communicating across a massive NVLink interconnect fabric that behaves as a unified, coherent entity.8 Consequently, the traditional boundaries separating hardware engineering disciplines have collapsed. Historically, microarchitects operated strictly within the logical domain, drafting specifications and writing register-transfer level (RTL) code to maximize instructions per cycle (IPC).9 Concurrently, physical design engineers operated in the spatial domain, synthesizing that logic into physical gates, placing them on a die, routing the interconnections, and battling timing constraints and voltage drop.9

Today, those silos present a critical liability. An architectural decision to widen a tensor processing pipeline directly influences the routing congestion and dynamic power density during the physical place-and-route phase. Conversely, the physical realities of thermal hotspots in advanced 2.5D and 3D packaging dictate the maximum viable clock frequencies, forcing architects to fundamentally rethink their dataflow and parallelism strategies.11 This convergence has birthed an intense industry demand for hybrid engineers—professionals who possess the theoretical rigor to architect complex, high-performance systems and build cycle-accurate software models, combined with the pragmatic physical design expertise to navigate the treacherous realities of tape-outs on advanced process nodes.13

This report presents an exhaustive, expert-level roadmap engineered specifically to navigate this converged landscape over the next twelve to eighteen months. By systematically rebuilding foundational knowledge through the curricula of elite institutions—such as the University of Michigan, Stanford University, and the Massachusetts Institute of Technology—and subsequently executing highly targeted, cross-domain technical projects, an engineer can construct a demonstrably elite profile. This strategic progression is calibrated not only to secure a position at NVIDIA but to establish the candidate as an indispensable architect of the platforms that will power the next decade of agentic artificial intelligence.

## Deconstructing the Hybrid Architecture and Physical Design Mandate

To successfully chart a trajectory toward a hybrid hardware role, it is imperative to precisely decode the technical expectations and operational realities of these positions within NVIDIA's contemporary organizational structure. Roles bearing titles such as Graphics Architect, System-on-Chip (SoC) Methodology Architect, ASIC Physical Design and Timing Engineer, and Full Stack Software Engineer for GPU Architecture increasingly overlap in their requisite skill sets.14 An engineer targeting this intersection must demonstrate fluency across four distinct but interconnected technical vectors.

### Microarchitecture and Register-Transfer Level Implementation
The core language of hardware remains the hardware description language (HDL), specifically Verilog and SystemVerilog.15 A hybrid engineer must possess the capability to translate complex algorithmic concepts into high-performance, area-efficient, and power-optimized RTL.19 This extends far beyond rudimentary finite state machines (FSMs). It involves the meticulous design of deeply pipelined execution units, intricate memory hierarchies, complex arbiters for shared resources, round-robin schedulers, and sophisticated synchronization primitives.20 Furthermore, the candidate must be intimately familiar with the dangers of asynchronous data transfers, possessing a robust understanding of clock domain crossing (CDC) techniques, synchronization FIFOs, and the mitigation of metastable states.15 In the hybrid paradigm, the RTL must be written with acute spatial awareness; the designer must intuitively anticipate how the logic will map to physical standard cells and how the depth of combinatorial logic paths will impact timing closure.

### Performance Modeling and Software Engineering
Before a single line of RTL is synthesized, NVIDIA relies upon exhaustive software simulation to validate architectural theories and quantify projected performance gains.13 Hybrid roles demand exceptional software engineering proficiency, primarily utilizing modern C++ to construct cycle-accurate functional and performance models.14 These discrete-event simulators model the complex interactions of GPU sub-systems, allowing architects to explore vast design spaces and evaluate trade-offs related to latency, bandwidth, and power consumption across varying deep learning and graphics workloads.21 Additionally, automation is a cornerstone of modern chip design. Engineers must be highly proficient in scripting languages such as Python, Perl, and Tool Command Language (Tcl) to develop tools that analyze simulation outputs, automate verification regressions, and interface directly with complex electronic design automation databases.15

### Physical Implementation and Timing Closure
The distinguishing characteristic of the hybrid engineer is their mastery of the physical domain. This involves driving the physical implementation flow from a synthesized gate-level netlist to a final GDSII layout ready for foundry fabrication.10 The engineer must understand the intricacies of floorplanning, which involves the strategic placement of macro blocks (such as SRAM arrays) and the definition of the die's core area to minimize wire lengths and alleviate routing congestion.18 Furthermore, the candidate must command the mathematics of Static Timing Analysis (STA).26 They must be capable of calculating arrival times, required times, and timing slack, while navigating the complexities of clock tree synthesis (CTS), clock skew, and the detrimental effects of jitter.28 Resolving setup and hold violations by strategically resizing standard cells, inserting buffer chains, or restructuring logic paths is a fundamental daily operation.27

### System-Level Constraints and Advanced Packaging
A modern NVIDIA accelerator is a heterogeneous assembly of diverse functional chiplets.5 Therefore, a hybrid architect must possess a systems-level perspective that encompasses advanced packaging technologies, power delivery, and high-speed input/output protocols.19 They must understand the physics of signal integrity over transmission lines, the thermal dissipation challenges inherent in 2.5D and 3D vertical stacking, and the implications of coefficient of thermal expansion (CTE) mismatches that induce physical package warpage.12 Furthermore, familiarity with high-speed interface standards such as Peripheral Component Interconnect Express (PCIe), Universal Chiplet Interconnect Express (UCIe), and the signaling layers of the Open Systems Interconnection (OSI) stack is increasingly mandated.5

## Academic Foundations and the Strategic Knowledge Refresher

To operate at the zenith of the hardware industry, an engineer cannot rely solely on the practical application of software tools; they must possess a profound, mathematically rigorous understanding of the underlying physics of computation. Building upon a foundation of undergraduate coursework—specifically the University of Michigan's EECS 370, EECS 373, and EECS 470—the candidate must execute a comprehensive knowledge refresher and expansion.35 This phase must aggressively synthesize advanced concepts from the graduate curricula of MIT and Stanford University to ensure total parity with the intellectual vanguard of the field.

### Rebuilding the Core: Advanced Computer Architecture
The University of Michigan's EECS 370 (Introduction to Computer Organization) and EECS 470 (Computer Architecture) provide the critical theoretical framework for processor design.35 EECS 370 introduces the foundational concepts of instruction set architectures (ISA), datapath construction, basic pipelining, and the stored-program concept, bridging high-level C programming with low-level assembly execution.36 EECS 470 escalates this by exploring the complex microarchitectural mechanisms that enable high-performance uniprocessor execution.37

To refresh and vastly upgrade this knowledge base, the candidate must revisit the intricacies of out-of-order (OOO) execution, superscalar design, and speculative execution.38 They must thoroughly understand the mechanics of Tomasulo's algorithm, the function of the Reorder Buffer (ROB) in maintaining precise exception states, and the role of physical register files in register renaming to eliminate false data dependencies.

However, modern AI workloads are heavily reliant on massive parallel processing rather than single-thread latency optimization. Therefore, the candidate must delve into the materials provided by MIT's 6.5900 (Computer System Architecture).39 This graduate-level course provides exhaustive coverage of multithreaded architectures, cache coherence protocols (such as MESI and directory-based schemes), memory consistency models, and the design of vector supercomputers.39 Furthermore, Stanford's EE282 (Computer Systems Architecture) offers vital perspectives on the interaction between hardware and system software, covering advanced memory hierarchies, virtualization, and performance analysis at the cluster and data-center scale.42 The defining objective of this architectural review is to inherently grasp the power and area trade-offs associated with complex speculative structures, thereby understanding why highly parallel, throughput-oriented architectures dominate the modern GPU landscape.

### Mastery of VLSI Systems and Physical Realities
To bridge the gap between logical architecture and physical hardware, a deep theoretical understanding of Very-Large-Scale Integration (VLSI) is mandatory. While UMich's EECS 427 (VLSI Design I) introduces mask-level CMOS layout and static CMOS circuit delay 44, the hybrid engineer requires a sophisticated understanding of digital abstraction and synthesis.

Stanford's EE271 (Introduction to VLSI Systems) is the premier resource for this transition.46 The curriculum systematically moves from the device physics of MOS transistors to the construction of abstractions that allow for reasoning about complex digital systems.46 A critical component of this study is the method of logical effort, a technique used to estimate delay in CMOS circuits and optimize the sizing of logic gates for maximum speed.48 An architect versed in logical effort can look at an RTL datapath and intuitively predict whether it will meet timing constraints long before the synthesis tools are invoked. The course also extensively covers design for testability (DFT), dynamic verification, and the synthesis of physical layouts directly from SystemVerilog descriptions.47

Simultaneously, the candidate must internalize the electrical realities of high-speed systems by studying Stanford's EE273 (Digital Systems Engineering).33 As clock frequencies escalate and operating voltages plummet, digital signals increasingly exhibit analog behaviors. This course covers the fundamental physics of ideal and non-ideal transmission lines, wave propagation, and impedance matching.50 The candidate must master the analysis of timing noise (skew and jitter), the causes of crosstalk, and the critical importance of designing robust on-chip power distribution networks to mitigate simultaneous switching noise and voltage droop.33 This electrical foundation is vital for any engineer designing the physical interfaces between chiplets or planning the floorplan of a multi-die package.

### Domain-Specific Architectures and Hardware/Software Codesign
NVIDIA's dominance is predicated on specialized hardware acceleration for artificial intelligence. Consequently, a generic understanding of computer architecture is insufficient; the candidate must pivot toward domain-specific accelerators. Stanford's CS217 (Hardware Accelerators for Machine Learning) provides a comprehensive framework for designing modern AI processing units.51 The course dissects dataflow architectures, tensor processing mechanics, and the profound impact of data precision (such as FP8 and FP4) and network sparsity on hardware efficiency.51

Complementing this is MIT's 6.5930 (Hardware Architecture for Deep Learning), which emphasizes the co-optimization of algorithms and hardware.52 The curriculum covers spatial architectures, systolic array mapping techniques, and emerging technologies like compute-in-memory (CiM).52 By studying these resources, the engineer learns how to map complex neural network topologies onto silicon structures, strategically minimizing the energy-intensive movement of data between processing elements and global memory.

### Interconnection Networks and Fabric Design
The era of the monolithic chip has been superseded by disaggregated architectures relying on massive communication fabrics. Understanding how data travels between processors, memory modules, and independent chiplets is crucial. Stanford's EE382C (Interconnection Networks) provides the definitive theoretical background.54 The candidate must master the taxonomy of network topologies (including meshes, tori, and flattened butterflies), routing algorithms, and the critical mechanisms of credit-based flow control.54 Deep knowledge of router microarchitecture—specifically virtual channel allocation, switch arbitration, and the prevention of routing deadlock—is a non-negotiable prerequisite for an engineer aspiring to develop or optimize interconnects analogous to NVIDIA's proprietary NVLink and NVSwitch technologies.8

## Navigating the Edge of Technological Advancement: The 2026 Landscape

To ensure this roadmap remains highly targeted and immune to technological volatility, the candidate's strategic focus must align flawlessly with the inflection points defining the 2026 semiconductor industry. NVIDIA's transition to the Vera Rubin architecture serves as the definitive blueprint for the future of extreme hardware engineering.2 A hybrid engineer must internalize the specifications, constraints, and innovations of this platform to demonstrate immediate value to hiring managers.

### The Vera Rubin Rack-Scale Paradigm
The Rubin platform marks a definitive shift away from localized node optimization toward true data-center-scale engineering.2 The flagship Vera Rubin NVL72 system is an integrated marvel, combining 72 Rubin GPUs and 36 custom Vera CPUs within a single rack, orchestrated by advanced networking components including ConnectX-9 SuperNICs and BlueField-4 Data Processing Units (DPUs).7

The Rubin GPU itself is an engineering colossus, fabricated on TSMC's cutting-edge N3 process node and containing 336 billion transistors spread across dual compute dies.2 For an architect, the defining feature of the Rubin GPU is the third-generation Transformer Engine, which incorporates hardware-accelerated adaptive compression and fine-grained micro-tensor scaling to deliver an unprecedented 50 PFLOPS of inference performance utilizing the NVFP4 (4-bit floating point) data format.1 Understanding the algorithmic implications of reduced-precision arithmetic, and how to design datapath logic that maintains computational accuracy while drastically reducing silicon area and dynamic power consumption, is a highly prized skill set for 2026.1 Furthermore, the introduction of the Rubin CPX variant, designed explicitly to handle massive long-context inference tasks using highly compute-dense structures, highlights the ongoing divergence and specialization of architectural profiles within a single generation.59

### The Memory Wall and Advanced Interconnect Fabrics
As AI models scale into the trillions of parameters, performance is entirely gated by memory bandwidth and the speed of inter-chip communication. The Rubin architecture attacks this bottleneck through massive spatial integration. Each Rubin GPU is paired with up to 288 GB of sixth-generation High Bandwidth Memory (HBM4), achieving an aggregate bandwidth of 22 terabytes per second (TB/s) through deep co-engineering with memory ecosystems and optimized physical controllers.2

Simultaneously, the Vera CPU—built upon the ARM v9.2 architecture—eschews the traditional, latency-inducing PCIe bus.7 Featuring 88 custom NVIDIA Olympus cores, the Vera CPU connects directly to the Rubin GPUs via the NVLink-C2C interface, delivering 1.8 TB/s of coherent, high-bandwidth memory access.6 At the macro level, the sixth-generation NVLink fabric provides an astounding 3.6 TB/s of all-to-all scale-up bandwidth per GPU, enabling the massive parallelization required for MoE model training.7

For a hybrid engineer, these specifications dictate a mandatory fluency in high-speed serializer/deserializer (SerDes) design, coherent memory protocols, and the physical constraints of dense interconnect routing.54 Furthermore, the industry-wide transition toward Co-Packaged Optics (CPO) and silicon photonics—aimed at replacing copper interconnects to mitigate signal attenuation at the rack scale—represents a massive area of ongoing research and physical design complexity.62

### Thermo-Mechanical Constraints and 3D Packaging
The staggering density of the Rubin architecture exacerbates the physical realities of power delivery and thermal management. A single NVL72 rack pushes power consumption well beyond 100 kilowatts, rendering traditional air cooling entirely obsolete and mandating direct-to-chip liquid cooling architectures.61

The physical integration of dual compute dies, Vera CPUs, and multiple stacks of HBM4 relies heavily on advanced packaging techniques, predominantly TSMC's CoWoS-L (Chip-on-Wafer-on-Substrate with Local Silicon Interconnect) and precise wafer-to-wafer hybrid bonding.7 A physical design engineer must navigate a labyrinth of thermo-mechanical challenges in this environment. Assembling heterogeneous dies introduces severe coefficient of thermal expansion (CTE) mismatches, leading to package warpage and mechanical stress during thermal cycling.12 Furthermore, supplying hundreds of amperes of current at sub-1V operating voltages into a dense 3D package creates massive voltage drop (IR drop) anomalies within the Power Delivery Network (PDN).12 A competitive candidate must demonstrate the ability to co-simulate thermal densities, mechanical stress, and electrical parasitics during the earliest stages of floorplanning.11

| Architectural Specification | NVIDIA Blackwell Generation | NVIDIA Rubin Generation |
| :--- | :--- | :--- |
| **Manufacturing Process** | TSMC 4NP | TSMC N3 |
| **Transistor Count (GPU)** | 208 Billion | 336 Billion |
| **Memory Technology** | HBM3e | HBM4 |
| **Maximum GPU Memory** | 192 GB | 288 GB |
| **Peak Memory Bandwidth** | 8 TB/s | 22 TB/s |
| **NVLink GPU-to-GPU Bandwidth** | 1.8 TB/s | 3.6 TB/s |
| **Peak AI Inference (NVFP4)** | N/A | 50 PFLOPS |

Table 1: A comparative analysis of physical and architectural scaling from the Blackwell to the Rubin generation, highlighting the exponential increase in memory bandwidth and interconnect velocity required for modern AI workloads.1

## High-Impact, Cross-Domain Portfolio Engineering

Academic credentials and theoretical knowledge must be substantiated by demonstrable execution. To stand out in NVIDIA's highly competitive recruitment ecosystem, the candidate must develop a portfolio of complex, open-ended engineering projects. Standard undergraduate assignments, such as simple MIPS emulators or basic Arduino applications, are entirely insufficient for 2026.66 The portfolio must explicitly target the intersection of parallel architecture, physical design constraints, and modern automation flows, proving cross-domain applicability.

### Project 1: RTL-to-GDSII Tapeout of a Sparse Tensor Accelerator Core
**Objective:** Design, verify, and execute the full physical synthesis flow for a highly parallel, machine-learning-focused hardware accelerator using industry-standard open-source EDA tools. 
**Execution Strategy:** The candidate will utilize the OpenLane EDA infrastructure and the SkyWater 130nm (or an equivalent modern open) Process Design Kit (PDK).24 The project initiates in the architectural domain: writing synthesizable SystemVerilog for a parameterized systolic array optimized for matrix multiplication, specifically incorporating control logic to handle sparse data structures (skipping zero-value multiplications to save power).52 Following rigorous functional verification using testbenches and SystemVerilog assertions, the candidate will drive the design through the complete physical ASIC flow: Logic Synthesis (Yosys), Floorplanning and Power Planning (OpenROAD), Placement and Clock Tree Synthesis (TritonCTS), and Routing and Sign-off Analysis (OpenSTA, Magic).24 
**Strategic Value:** This project is the ultimate proof of hybrid capability. It demonstrates that the candidate can conceptualize a complex mathematical accelerator and successfully navigate the punishing physical realities of timing closure, power distribution, and spatial layout constraints.

### Project 2: Cycle-Accurate C++ Performance Simulator for Rack-Scale Interconnects
**Objective:** Architect and develop a highly parameterized, discrete-event software simulator modeling a scalable network-on-chip (NoC) or die-to-die fabric, mirroring the architectural challenges of NVIDIA's NVLink and NVSwitch. 
**Execution Strategy:** Utilizing modern, high-performance C++, the candidate will build a simulator capable of modeling various network topologies (e.g., 2D mesh, flattened butterfly, or torus).41 The simulator must model deep microarchitectural specifics, including Virtual Channel Management (credit-based flow control), Switch Arbitration (allocators like iSLIP), and Synthetic Traffic Generation.54 
**Strategic Value:** This project forcefully highlights the software engineering proficiency required of hardware architects. It proves the candidate can write clean, object-oriented C++ and utilize data to drive architectural decisions, allowing them to generate latency-versus-throughput curves to justify the superiority of one routing algorithm over another.13

### Project 3: Thermal and Power-Aware Hardware/Software Co-Design for HBM Interface
**Objective:** Implement a High Bandwidth Memory (HBM) controller in RTL, coupled with a quantitative analysis of power-performance trade-offs under simulated 2.5D packaging thermal constraints. 
**Execution Strategy:** The candidate will design a simplified memory controller in Verilog that manages multiple parallel memory channels, request scheduling, and page activation policies.39 The critical differentiator of this project is the integration of power and thermal modeling. Using analytical models or open-source EDA plugins, the candidate will estimate the dynamic and leakage power of the controller under aggressive access patterns, concluding with a whitepaper analyzing power vs. frequency trade-offs in 2.5D packages like CoWoS.11 
**Strategic Value:** This project attacks the exact memory bandwidth and thermal limitations defining the Rubin era.2 It demonstrates a mature, cross-disciplinary perspective that values performance-per-watt and thermo-mechanical viability as highly as raw computational throughput.

## Navigating the NVIDIA Interview Crucible: Preparation and Tactics

The interview process at NVIDIA is famously rigorous, meticulously designed to evaluate a candidate's theoretical depth, practical coding proficiency, and ability to reason through complex system-level constraints.29 For a hybrid architecture and physical design role, the evaluation will seamlessly pivot between digital logic puzzles, timing mathematics, software engineering, and broad architectural theory.29

### Digital Logic and RTL Fundamentals
Technical screenings frequently rely on intricate hardware design puzzles.29 The candidate must be prepared to write clean, synthesizable Verilog on a whiteboard or shared coding environment. Interviewers will provide convoluted behavioral specifications requiring the design of highly optimized Mealy or Moore state machines, probing for knowledge of state encoding (e.g., one-hot vs. binary) and transition logic efficiency.29 Clock Domain Crossing (CDC) is a critical area; the candidate must fluently explain synchronizer chains, handshaking protocols, and the detailed microarchitecture of an asynchronous FIFO, specifically highlighting the necessity of Gray code counters to prevent metastable states.15

### Static Timing Analysis and Physical Realities
NVIDIA explicitly tests an architect's comprehension of physical design implications.28 The candidate must possess a mathematically rigorous understanding of timing closure. Be prepared to draw complex timing waveforms, identify critical paths, and calculate setup and hold slacks incorporating parameters for clock jitter, clock skew, combinatorial logic delay, and flip-flop propagation delays (clock-to-Q).28 When presented with a schematic exhibiting a timing violation, the candidate must articulate a hierarchy of solutions, such as utilizing faster standard cells, reducing fan-out via buffer insertion, restructuring combinatorial logic, or exploiting useful clock skew.30

### Computer Architecture and System-Level Trade-offs
The architectural phase of the interview shifts focus toward quantitative analysis, execution models, and data movement. Questions will probe the design of multi-level cache systems, the nuances of cache coherence protocols (such as MESI/MOESI), and the performance discrepancies between on-chip SRAM and off-chip HBM.76 The candidate must be capable of diagramming an out-of-order execution pipeline, fluently explaining the roles of the reorder buffer, reservation stations, and register renaming hardware.41 System scaling questions, such as designing the distributed training infrastructure for a massive parameter LLM, require discussing the interplay of compute node density and the bandwidth limitations of NVLink versus InfiniBand.61

### Software Engineering and Algorithmic Proficiency
Despite the hardware focus, NVIDIA mandates strong programming proficiency, primarily in C/C++ and Python.15 Candidates must maintain a rigorous practice schedule for algorithmic problem-solving (e.g., LeetCode mediums), focusing on arrays, graphs, trees, and linked lists.75 Performing accurate time and space complexity analyses (Big O notation) is absolutely essential.75 Understanding multithreading, mutexes, locks, and parallelism at the operating system level is critical for engineers writing efficient simulation software or optimizing highly parallel GPU architectures.73

## Detailed 12-Month Weekly Strategic Roadmap

This comprehensive roadmap translates the theoretical imperatives into an actionable, week-by-week execution plan. It utilizes open-source courseware from UMich, Stanford, and MIT.

### Phase 1: Rebuilding the Foundation & Theoretical Refresher (Months 1-3)
**Goal:** Solidify computer architecture, digital logic, and physical design fundamentals.

#### Month 1: Advanced Microarchitecture & Digital Logic
* **Week 1: Pipeline & Speculation Basics**
    * **Task:** Review UMich(https://eecs370.github.io/) 36 and(https://www.eecs.umich.edu/courses/eecs470/) 81 lecture materials.
    * **Goal:** Re-master instruction set architectures, standard 5-stage pipelines, and basic hazards.
    * **Coding:** Implement a simple single-cycle MIPS or ARM processor in SystemVerilog.
* **Week 2: Out-of-Order (OoO) Execution**
    * **Task:** Deep dive into Tomasulo's Algorithm, Reorder Buffers (ROB), and Register Renaming (EECS 470).38
    * **Goal:** Be able to draw an OoO pipeline from memory and map data dependencies.
* **Week 3: Advanced State Machines & Logic Puzzles**
    * **Task:** Study FSM optimization (Mealy vs. Moore) and state encoding (binary, Gray, one-hot).
    * **Coding:** Write synthesizable RTL for a parameterized round-robin arbiter.
* **Week 4: Clock Domain Crossing (CDC) & Async FIFOs**
    * **Task:** Study synchronizers, metastability, and handshaking protocols.
    * **Goal:** Design a robust Asynchronous FIFO in Verilog using Gray code pointers. Write a testbench to verify cross-domain data integrity.

#### Month 2: VLSI Systems & Physical Realities
* **Week 5: CMOS Transistors & Delay Modeling**
    * **Task:** Begin Stanford(https://online.stanford.edu/courses/ee271-introduction-vlsi-systems).47 Study switch-resistor models and physical layouts.
    * **Goal:** Calculate theoretical propagation delays for basic logic gates.
* **Week 6: Logical Effort & Sizing Optimization**
    * **Task:** Master the method of Logical Effort to minimize delay across combinatorial logic paths (EE271).48
    * **Goal:** Optimize a multi-stage decoding circuit purely through mathematical cell sizing.
* **Week 7: Static Timing Analysis (STA) Math**
    * **Task:** Review setup time, hold time, and clock-to-Q equations.
    * **Goal:** Practice drawing timing waveforms and manually calculating slack across standard flip-flops considering clock skew and jitter.
* **Week 8: High-Speed Digital Design Constraints**
    * **Task:** Review Stanford(https://online.stanford.edu/courses/ee273-digital-systems-engineering).49
    * **Goal:** Understand transmission line physics, characteristic impedance, crosstalk, and the impact of simultaneous switching noise (SSN) on Power Delivery Networks (PDN).

#### Month 3: Advanced Systems, Parallelism, & Coherence
* **Week 9: Multithreading & Cache Coherence**
    * **Task:** Study MIT(https://csg.csail.mit.edu/6.5900/).82 Focus on MESI/MOESI cache coherence protocols.41
    * **Goal:** Diagram memory consistency models and explain false sharing.
* **Week 10: Vector Processors & GPUs**
    * **Task:** Transition to parallel computing hardware. Review SIMD, SIMT, and vector processing architectures (MIT 6.5900).41
    * **Goal:** Understand the architectural differences between latency-optimized CPUs and throughput-optimized GPUs.
* **Week 11: Parallel Software Models**
    * **Task:** Review Stanford(https://cs149.stanford.edu/).
    * **Goal:** Write a basic CUDA kernel (e.g., Matrix Multiplication) to understand how hardware blocks (thread blocks, warps) map to software.
* **Week 12: Phase 1 Consolidation & Review**
    * **Task:** Synthesize notes from UMich, Stanford, and MIT courses.
    * **Goal:** Complete a mock "whiteboard" interview focusing strictly on OoO architecture and STA equations.

### Phase 2: Architecture Modeling & Software Simulation (Months 4-6)
**Goal:** Develop elite C++ skills and build cycle-accurate simulation infrastructure.

#### Month 4: C++ Mastery & Simulator Scaffolding
* **Week 13: Modern C++ for Hardware Engineers**
    * **Task:** Refresher on C++17/20 features: smart pointers, lambda expressions, concurrency primitives (mutexes, locks).73
    * **Goal:** Setup the build environment (CMake, Git) for Project 2 (Cycle-Accurate C++ NoC Simulator).
* **Week 14: Network-on-Chip (NoC) Topologies**
    * **Task:** Study Stanford EE382C: Interconnection Networks.55
    * **Goal:** Implement the basic C++ object models for Routers, Links, and Flits. Define a 2D-Mesh topology.
* **Week 15: Routing Algorithms**
    * **Task:** Study XY routing, dimension-order routing, and deadlock avoidance.83
    * **Goal:** Code the routing logic module within the simulator.
* **Week 16: Virtual Channels & Flow Control**
    * **Task:** Study credit-based flow control.83
    * **Goal:** Implement virtual channel buffer management in C++ to prevent network starvation.

#### Month 5: Advanced Simulator Features
* **Week 17: Switch Arbitration (iSLIP)**
    * **Task:** Research crossbar arbitration techniques.
    * **Goal:** Implement an iSLIP or round-robin allocator in C++ for the router microarchitecture.
* **Week 18: Synthetic Traffic Generation**
    * **Task:** Model specific workload patterns (uniform random, bit-complement, all-to-all).
    * **Goal:** Build a traffic injection engine that accurately mimics AI model communication bursts.
* **Week 19: Metric Collection & Profiling**
    * **Task:** Add instrumentation to the simulator.
    * **Goal:** Track average flit latency, network throughput, and buffer utilization metrics.
* **Week 20: Project 2 Finalization & Documentation**
    * **Task:** Run scaling experiments (e.g., 4x4 vs 8x8 mesh).
    * **Goal:** Generate latency-throughput curves and write a 3-page technical whitepaper detailing the architectural trade-offs. Publish to GitHub.

#### Month 6: Deep Learning Architectures (Hardware/Software Co-design)
* **Week 21: Tensor Processing Mechanics**
    * **Task:** Study Stanford(https://cs217.stanford.edu/) 51 and MIT(https://csg.csail.mit.edu/6.5930/).84
    * **Goal:** Understand spatial architectures, dataflow mapping (weight-stationary vs. output-stationary), and MAC arrays.53
* **Week 22: Sparsity and Low-Precision Arithmetic**
    * **Task:** Analyze how INT8 and FP4 precisions reduce area and power.51
    * **Goal:** Draft the microarchitectural specification for Project 1 (Sparse Tensor Accelerator).
* **Week 23: RTL Implementation of Systolic Arrays**
    * **Task:** Begin writing SystemVerilog for a parameterized 4x4 or 8x8 systolic array.71
    * **Goal:** Implement processing elements (PEs) capable of zero-skipping (sparsity).
* **Week 24: Functional Verification**
    * **Task:** Write a comprehensive testbench.
    * **Goal:** Verify the tensor accelerator using random stimulus and edge cases. Ensure 100% functional coverage.

### Phase 3: Physical Design Execution & EDA Fluency (Months 7-9)
**Goal:** Execute an end-to-end ASIC tapeout flow using Open-Source tools.

#### Month 7: Logic Synthesis & Floorplanning
* **Week 25: OpenLane & Sky130 Environment Setup**
    * **Task:** Install the OpenLane EDA toolchain and SkyWater 130nm PDK (Linux/Docker).24
    * **Goal:** Successfully run the flow on a simple baseline design (e.g., PicoRV32) to verify the toolchain.31
* **Week 26: Logic Synthesis (Yosys)**
    * **Task:** Push the Systolic Array RTL from Project 1 through Yosys.
    * **Goal:** Analyze the generated gate-level netlist. Review logic depth and identify potential critical paths.
* **Week 27: Macro Placement & Floorplanning**
    * **Task:** Utilize OpenROAD to define the silicon die area and pin placement.24
    * **Goal:** Strategically place memory macros to minimize wire length to the processing elements.
* **Week 28: Power Planning (PDN)**
    * **Task:** Design the Power Distribution Network.
    * **Goal:** Create a robust power grid (VDD/VSS rings and stripes) to prevent IR drop across the dense MAC array.30

#### Month 8: Placement, Clocking, & Routing
* **Week 29: Standard Cell Placement**
    * **Task:** Execute global and detailed placement of standard cells.
    * **Goal:** Review placement density and congestion heatmaps. Adjust floorplan if routing congestion is too high.
* **Week 30: Clock Tree Synthesis (CTS)**
    * **Task:** Use TritonCTS to build the clock distribution network.70
    * **Goal:** Synthesize a balanced clock tree. Analyze clock skew and insertion delay across the tensor core.
* **Week 31: Routing (Global & Detailed)**
    * **Task:** Execute the routing phase.24
    * **Goal:** Resolve any routing violations, DRC (Design Rule Check) errors, or shorts.
* **Week 32: Parasitic Extraction (RC)**
    * **Task:** Extract resistance and capacitance values from the routed layout.
    * **Goal:** Prepare the SPEF file required for accurate physical timing analysis.

#### Month 9: Timing Closure & Sign-off
* **Week 33: Static Timing Analysis (OpenSTA)**
    * **Task:** Run post-route STA using OpenSTA.70
    * **Goal:** Identify Setup and Hold violations resulting from physical routing delays.
* **Week 34: Resolving Timing Violations**
    * **Task:** Perform Engineering Change Orders (ECOs).
    * **Goal:** Upsize cells to fix setup violations; insert delay buffers to fix hold violations. Re-route and re-verify.
* **Week 35: Physical Verification (DRC & LVS)**
    * **Task:** Use Magic to run final DRC and Layout vs. Schematic (LVS) checks.24
    * **Goal:** Achieve a completely clean physical layout.
* **Week 36: GDSII Generation & Portfolio Documentation**
    * **Task:** Generate the final GDSII file.
    * **Goal:** Document the entire flow, highlighting the PPA (Power, Performance, Area) trade-offs made during timing closure. Publish Project 1 to GitHub.

### Phase 4: Advanced Packaging, Edge-of-Art Tech, & Interview Prep (Months 10-12)
**Goal:** Master 2026 NVIDIA-specific architectures and conquer the interview crucible.

#### Month 10: Thermal constraints & HBM Co-Design
* **Week 37: HBM4 & Advanced Memory Protocols**
    * **Task:** Research HBM4 specifications (22 TB/s bandwidth, 2.5D stacking) and memory controller design.6
    * **Goal:** Draft RTL for a simplified memory controller (Project 3).
* **Week 38: 2.5D/3D Packaging (CoWoS-L)**
    * **Task:** Study TSMC's CoWoS-L and hybrid bonding techniques.32 Understand CTE mismatches and thermal density.
    * **Goal:** Write a simulation script evaluating how increased switching frequency in the HBM controller impacts dynamic power and localized thermal hotspots.85
* **Week 39: The Vera Rubin Architecture Deep Dive**
    * **Task:** Analyze NVIDIA's Rubin whitepapers. Study the Vera CPU (88 cores), NVLink 6 (3.6 TB/s), and the 50 PFLOPS NVFP4 Transformer Engine.6
    * **Goal:** Be able to explicitly articulate why NVIDIA uses "extreme codesign" at the rack scale (NVL72).6
* **Week 40: Silicon Photonics & CPO**
    * **Task:** Research Co-Packaged Optics (CPO) and how light-in/light-out systems replace copper in AI clusters.62
    * **Goal:** Understand the physical constraints of integrating optical engines with silicon dies.

#### Month 11: Interview Conditioning (Coding & Algorithms)
* **Week 41: Data Structures & Algorithms (Python/C++)**
    * **Task:** Begin intensive LeetCode practice (Arrays, Strings, Hash Maps).73
    * **Goal:** Solve 2-3 Mediums daily. Focus on optimal Big-O time/space complexity.
* **Week 42: Graph Algorithms & Linked Lists**
    * **Task:** Practice DFS, BFS, and Linked List manipulations (e.g., Reverse Linked List, LRU Cache).74
    * **Goal:** Achieve a 20-minute solve rate for Medium difficulty problems.
* **Week 43: Systems Software & OS Fundamentals**
    * **Task:** Review memory management, virtual memory, paging, and kernel vs. user space.87
    * **Goal:** Be prepared for low-level systems questions.
* **Week 44: Concurrency & Multithreading**
    * **Task:** Practice writing thread-safe code.73
    * **Goal:** Explain deadlock, race conditions, and implement basic locking mechanisms.

#### Month 12: Interview Conditioning (Hardware & Final Prep)
* **Week 45: Rapid-Fire Digital Logic & RTL**
    * **Task:** Practice whiteboard RTL coding (FSMs, Arbiters, FIFOs).29
    * **Goal:** Write clean, bug-free, synthesizable Verilog under a 15-minute time constraint.
* **Week 46: STA and Physical Design Grilling**
    * **Task:** Review all timing closure math and physical design concepts (antenna effects, electromigration, IR drop).
    * **Goal:** Be able to vocally troubleshoot a failing timing path or routing congestion issue on the fly.29
* **Week 47: System Design & Architecture Scenarios**
    * **Task:** Practice high-level architecture questions (e.g., "Design a memory allocator," "Design the topology for a trillion-parameter LLM training cluster").74
    * **Goal:** Demonstrate the ability to balance power, latency, and area at the macro level.
* **Week 48: Resume Optimization & Application Strategy**
    * **Task:** Tailor your resume. Emphasize keywords like RTL Design, SystemVerilog, OpenLane, Physical Design, STA, Cycle-Accurate C++ Modeling.9
    * **Goal:** Apply to specific hybrid roles (e.g., Senior SoC Methodology Architect, Graphics Architect, ASIC Physical Design Engineer) and secure internal referrals.78

## Works cited
1. The Engine Behind AI Factories | NVIDIA Blackwell Architecture, accessed March 10, 2026, https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/
2. NVIDIA Rubin Finally Arrives, and Data Centers Will Never Be the Same Again | by Cogni Down Under | Jan, 2026, accessed March 10, 2026, https://medium.com/@cognidownunder/nvidia-rubin-finally-arrives-and-data-centers-will-never-be-the-same-again-2e5cd04d9d5b
3. 2024 Year in Review - Electrical and Computer Engineering, accessed March 10, 2026, https://ece.engin.umich.edu/wp-content/uploads/sites/4/2025/08/ece-magazine-2024.pdf
4. Challenges and prospects for advanced packaging - PMC - NIH, accessed March 10, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC11670716/
5. Chiplets and Advanced Packaging: Modular Integration for Next-Generation Electronics, accessed March 10, 2026, https://octopart.com/pulse/p/chiplets-and-advanced-packaging-modular-integration
6. Inside the NVIDIA Rubin Platform: Six New Chips, One AI Supercomputer, accessed March 10, 2026, https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
7. NVIDIA Kicks Off the Next Generation of AI With Rubin — Six New Chips, One Incredible AI Supercomputer, accessed March 10, 2026, https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer
8. Rack-Scale Agentic AI Supercomputer | NVIDIA Vera Rubin NVL72, accessed March 10, 2026, https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/
9. Invent the Future with Us. - NVIDIA, accessed March 10, 2026, https://www.nvidia.com/content/dam/en-zz/Solutions/careers/university-recruiting/corporate-web-hr-ur-digital-flyer-job-description.pdf
10. Nvidia Physical Design Jobs, Employment - Indeed, accessed March 10, 2026, https://www.indeed.com/q-nvidia-physical-design-jobs.html
11. 60 Computer Architecture Interview Questions - Final Round AI, accessed March 10, 2026, https://www.finalroundai.com/blog/computer-architecture-interview-questions
12. Chiplets: piecing together the next generation of chips (part I) - IMEC, accessed March 10, 2026, https://www.imec-int.com/en/articles/chiplets-piecing-together-next-generation-chips-part-i
13. Graphics Architect, Hardware - New College Grad 2026 - Careers at NVIDIA Corporation, accessed March 10, 2026, https://jobs.nvidia.com/careers/job/893393381000
14. GPU PCIe and Boot Architect - New College Grad 2026 - Careers at NVIDIA Corporation, accessed March 10, 2026, https://jobs.nvidia.com/careers/job/893393262026
15. Senior ASIC Design Engineer - Hardware - CAREERS AT NVIDIA, accessed March 10, 2026, https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-ASIC-Design-Engineer---Hardware_JR2008535
16. Nvidia Gpu Architecture Engineer Jobs, Employment | Indeed, accessed March 10, 2026, https://www.indeed.com/q-nvidia-gpu-architecture-engineer-jobs.html
17. Graphics Architect, Hardware - New College Grad 2026 - CAREERS AT NVIDIA, accessed March 10, 2026, https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Graphics-Architect--Hardware---New-College-Grad-2026_JR2013161
18. Senior SoC Methodology Architect, VLSI Physical Design - CAREERS AT NVIDIA, accessed March 10, 2026, https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-SoC-Methodology-Architect--VLSI-Physical-Design_JR2013596
19. ASIC Design Engineer - New College Grad (ASAP) at NVIDIA - Prosple, accessed March 10, 2026, https://prosple.com/graduate-employers/nvidia/jobs-internships/asic-design-engineer-new-college-grad
20. ASIC Design Engineer - New College Grad 2026 - Careers at NVIDIA Corporation, accessed March 10, 2026, https://jobs.nvidia.com/careers/job/893391566289
21. Senior GPU Power Architect - Careers at NVIDIA Corporation, accessed March 10, 2026, https://jobs.nvidia.com/careers/job/893392347743?domain=nvidia.com
22. ASIC Physical Design Engineer - Careers at NVIDIA Corporation, accessed March 10, 2026, https://jobs.nvidia.com/careers/job/893393253944
23. ASIC Hardware Design Engineer - New College Grad 2026 - Careers at NVIDIA Corporation, accessed March 10, 2026, https://jobs.nvidia.com/careers/job/893392917966
24. Newcomers - OpenLane Documentation, accessed March 10, 2026, https://openlane2.readthedocs.io/en/latest/getting_started/newcomers/index.html
25. Senior SoC Methodology Architect, VLSI Physical Design - Careers at NVIDIA Corporation, accessed March 10, 2026, https://jobs.nvidia.com/careers/job/893393550122
26. ASIC Physical Design Engineer - Careers at NVIDIA Corporation, accessed March 10, 2026, https://jobs.nvidia.com/careers/job/893392394355
27. ASIC Physical Design and Timing Engineer - New College Grad 2026 - CAREERS AT NVIDIA, accessed March 10, 2026, https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/ASIC-Timing-Engineer---New-College-Grad-2026_JR2013177
28. NVIDIA Hardware Engineer Interview: Process + Questions - Nora AI, accessed March 10, 2026, https://interview.norahq.com/interview-guides/nvidia-hardware-engineer-interview-guide-2025
29. NVIDIA Engineering Guide 2026 - Nora AI | AI Mock Interviewer, accessed March 10, 2026, https://interview.norahq.com/interview-guides/nvidia-asic-design-engineer-interview-guide-2026
30. aasthadave9/Advanced-Physical-Design-Using-OpenLANE-Sky130 - GitHub, accessed March 10, 2026, https://github.com/aasthadave9/Advanced-Physical-Design-Using-OpenLANE-Sky130
31. shariethernet/Physical-Design-with-OpenLANE-using-SKY130-PDK - GitHub, accessed March 10, 2026, https://github.com/shariethernet/Physical-Design-with-OpenLANE-using-SKY130-PDK
32. Current Advances and Outlook of Advanced Packaging - ASME Digital Collection, accessed March 10, 2026, https://asmedigitalcollection.asme.org/electronicpackaging/article/148/3/031010/1225361/Current-Advances-and-Outlook-of-Advanced-Packaging
33. EE273 Course | Stanford University Bulletin, accessed March 10, 2026, https://bulletin.stanford.edu/courses/1039101
34. Who Will Divide Up the CoWoS Production Capacity in 2026? - 36氪, accessed March 10, 2026, https://eu.36kr.com/en/p/3580962946874242
35. CSE Course Info | Computer Science and Engineering at Michigan, accessed March 10, 2026, https://cse.engin.umich.edu/academics/course-resources/cse-course-info/
36. EECS 370, accessed March 10, 2026, https://eecs370.github.io/
37. EECS 470: Computer Architecture, accessed March 10, 2026, https://www.eecs.umich.edu/courses/eecs470/eecs470-w25-Syllabus.pdf
38. EECS 470: Computer Architecture, accessed March 10, 2026, https://www.eecs.umich.edu/courses/eecs470/eecs470-f25-Syllabus-V2.pdf
39. Computer System Architecture | MIT Learn, accessed March 10, 2026, https://learn.mit.edu/search?resource=4275
40. 6.5900 [6.823] Computer System Architecture - Fall 2024, accessed March 10, 2026, https://csg.csail.mit.edu/6.5900/info.html
41. 6.5900 [6.823] Computer System Architecture - Fall 2024, accessed March 10, 2026, https://csg.csail.mit.edu/6.5900/lecnotes.html
42. CS 282: Computer Systems Architecture - Stanford University Explore Courses, accessed March 10, 2026, https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&q=CS%20282:%20Computer%20Systems%20Architecture&academicYear=20242025
43. Computer Systems Architecture | Course - Stanford Online, accessed March 10, 2026, https://online.stanford.edu/courses/ee282-computer-systems-architecture
44. EECS 427: VLSI Design I - Electrical and Computer Engineering, accessed March 10, 2026, https://ece.engin.umich.edu/academics/course-information/course-descriptions/eecs-427/
45. Electrical Engineering and Computer Science Courses (EECS) - Bulletin, accessed March 10, 2026, https://bulletin.engin.umich.edu/courses/eecs/
46. EE271 Course | Stanford University Bulletin, accessed March 10, 2026, https://bulletin.stanford.edu/courses/1039061
47. Introduction to VLSI Systems | Course - Stanford Online, accessed March 10, 2026, https://online.stanford.edu/courses/ee271-introduction-vlsi-systems
48. EE271 - VLSI Systems - Stanford University, accessed March 10, 2026, http://web.stanford.edu/class/ee271/
49. Digital Systems Engineering | Course - Stanford Online, accessed March 10, 2026, https://online.stanford.edu/courses/ee273-digital-systems-engineering
50. High speed digital system design : a handbook of interconnect theory and design practices, accessed March 10, 2026, https://searchworks.stanford.edu/view/4434452
51. Hardware Accelerators for Machine Learning (CS 217) - Stanford University, accessed March 10, 2026, https://cs217.stanford.edu/
52. Course Info - 6.5930/1 Hardware Architecture for Deep Learning - Spring 2026, accessed March 10, 2026, https://csg.csail.mit.edu/6.5930/info.html
53. Accelerator Architecture (Continued) : 6.5930/1 Hardware Architectures For Deep Learning | PDF | Central Processing Unit | Field Programmable Gate Array - Scribd, accessed March 10, 2026, https://www.scribd.com/document/790244629/L11
54. EE382C Course | Stanford University Bulletin, accessed March 10, 2026, https://bulletin.stanford.edu/courses/2042331
55. EE382C Advanced Computer Organization, accessed March 10, 2026, http://cva.stanford.edu/classes/ee382c/
56. EE382C Advanced Computer Organization: Interconnection Networks Course Policy and Information, accessed March 10, 2026, http://cva.stanford.edu/classes/ee382c/ee382c_spr05/handouts/policy.pdf
57. NVIDIA Rubin Enters Full Production | Introl Blog, accessed March 10, 2026, https://introl.com/blog/nvidia-rubin-full-production-ces-2026-ai-infrastructure
58. Infrastructure for Scalable AI Reasoning | NVIDIA Rubin Platform, accessed March 10, 2026, https://www.nvidia.com/en-us/data-center/technologies/rubin/
59. iPhone 17 Pro and 17 Pro Max hands-on: refreshing bold colors, soft matte unibody aluminum frame, and a nice two-tone back with a full-width camera bar (The Verge) - Techmeme, accessed March 10, 2026, https://www.techmeme.com/250909/p38
60. NVIDIA Unveils Rubin CPX: A New Class of GPU Designed for Massive-Context Inference, accessed March 10, 2026, https://nvidianews.nvidia.com/news/nvidia-unveils-rubin-cpx-a-new-class-of-gpu-designed-for-massive-context-inference
61. Rubin-Class Shift and Its Implications for AI Infrastructure | by elongated_musk - Medium, accessed March 10, 2026, https://medium.com/@Elongated_musk/rubin-class-shift-and-its-implications-for-ai-infrastructure-e66ce4cd61cc
62. Nvidia GTC 2026 Silicon Photonics Rubin Ultra Chip Launch CPO Data Center Infrastructure and Market Trends, accessed March 10, 2026, https://www.technetbooks.com/2026/03/nvidia-gtc-2026-silicon-photonics-rubin.html
63. Next-Gen HBM Architecture Detailed Including HBM4, HBM5, HBM6, HBM7 & HBM8: Up To 64 TB/s Bandwidth, 240 GB Capacity Per 24-Hi Stack, Embedded Cooling - Wccftech, accessed March 10, 2026, https://wccftech.com/next-gen-hbm-architecture-detailed-hbm4-hbm5-hbm6-hbm7-hbm8-up-to-64-tbps-bandwidth-240-gb-capacity-per-24-hi-stack-embedded-cooling/
64. Advanced Semiconductor Packaging 2025-2035: Forecasts, Technologies, Applications, accessed March 10, 2026, https://www.idtechex.com/en/research-report/advanced-semiconductor-packaging/1042
65. Power Delivery and Thermal-Aware Arm-Based Multi-Tier 3D Architecture, accessed March 10, 2026, https://gtcad.gatech.edu/www/papers/islped21-2.pdf
66. What are some embedded hobby projects that look good on a CV? - Reddit, accessed March 10, 2026, https://www.reddit.com/r/embedded/comments/l4mhgo/what_are_some_embedded_hobby_projects_that_look/
67. 6 RESUME PROJECTS That Will Actually Get You HIRED In 2026. - YouTube, accessed March 10, 2026, https://www.youtube.com/watch?v=f7ndZ-t9NPg
68. Which Projects should I put on my resume to get shortlisted? : r/FPGA - Reddit, accessed March 10, 2026, https://www.reddit.com/r/FPGA/comments/1hjt6kx/which_projects_should_i_put_on_my_resume_to_get/
69. VSD - A complete guide to install Openlane and Sky130nm PDK - Udemy, accessed March 10, 2026, https://www.udemy.com/course/vsd-a-complete-guide-to-install-openlane-and-sky130nm-pdk/
70. Advanced-Physical-Design-using-Openlane-Sky130 - VLSI System Design, accessed March 10, 2026, https://www.vlsisystemdesign.com/advanced-physical-design-using-openlane-sky130/
71. My Approach to Designing an AI Accelerator | by Srimanth Tenneti | Medium, accessed March 10, 2026, https://srimanthtenneti.medium.com/my-approach-to-designing-an-ai-accelerator-9d8d2af1f7f9
72. 6.823 Computer System Architecture - Fall 2021, accessed March 10, 2026, https://csg.csail.mit.edu/6.823F21/lecnotes.html
73. NVIDIA SWE Guide 2026 | Nora AI, accessed March 10, 2026, https://interview.norahq.com/interview-guides/nvidia-swe-interview-guide-2026
74. NVIDIA Software Engineer Interview Guide | Sample Questions (2026) - Exponent, accessed March 10, 2026, https://www.tryexponent.com/guides/nvidia-software-engineer-interview-guide
75. My 2026 NVDIA Software Engineer Interview and Questions - Linkjob AI, accessed March 10, 2026, https://www.linkjob.ai/interview-questions/nvidia-software-engineer-interview/
76. Nvidia Interview Process 2026 - Final Round AI, accessed March 10, 2026, https://www.finalroundai.com/blog/nvidia-interview-process
77. I Passed 2026 NVIDIA Technical Interview: Real Questions - Linkjob AI, accessed March 10, 2026, https://www.linkjob.ai/interview-questions/nvidia-technical-interview/
78. How to Get Hired at NVIDIA in 2026: Entry-Level Blueprint - LockedIn AI, accessed March 10, 2026, https://www.lockedinai.com/blog/get-hired-nvidia-2026-entry-level-blueprint
79. 1700 Questions Solved. Nvidia panel round experience. Senior SWE. : r/leetcode - Reddit, accessed March 10, 2026, https://www.reddit.com/r/leetcode/comments/1akv8i9/1700_questions_solved_nvidia_panel_round/
80. Nvidia Interview Questions (Updated 2026) - Exponent, accessed March 10, 2026, https://www.tryexponent.com/questions?company=nvidia
81. EECS 470: Computer Architecture - Fall 2025, accessed March 10, 2026, https://www.eecs.umich.edu/courses/eecs470/overview.html
82. 6.5900 [6.823] Computer System Architecture - Fall 2024 - MIT, accessed March 10, 2026, https://csg.csail.mit.edu/6.5900/
83. ee382c - Explore Courses - Stanford University, accessed March 10, 2026, https://explorecourses.stanford.edu/search?q=ee382c
84. 6.5930/1 Hardware Architecture for Deep Learning - Spring 2026, accessed March 10, 2026, https://csg.csail.mit.edu/6.5930/
85. Chiplet Fundamentals For Engineers: 2026 eBook, accessed March 10, 2026, https://semiengineering.com/knowledge_centers/packaging/multi-die-assemblies/chiplets/chiplets-deep-dive-into-designing-manufacturing-and-testing/
86. NVIDIA Unveils Rubin Platform to Support Large-Scale Training and Inference Workloads - AIwire - HPCwire, accessed March 10, 2026, https://www.hpcwire.com/aiwire/2026/01/06/nvidia-unveils-rubin-platform-to-support-large-scale-training-and-inference-workloads/
87. NVIDIA QA Engineer Interview Guide 2026 - Dataford, accessed March 10, 2026, https://dataford.io/interview-guides/nvidia/qa-engineer
88. Nvidia Asic Physical Design Jobs, Employment | Indeed, accessed March 10, 2026, https://www.indeed.com/q-nvidia-asic-physical-design-jobs.html
89. Senior Software R&D Engineer, VLSI Physical Design - Careers at NVIDIA Corporation, accessed March 10, 2026, https://jobs.nvidia.com/careers/job/893393562502
