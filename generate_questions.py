import json
import random

categories = {
    "Architecture": {
        "concepts": ["Reorder Buffer (ROB)", "Load Store Queue (LSQ)", "MESI protocol", "Superscalar execution", "Branch prediction", "Tomasulo's algorithm", "Cache coherence", "False sharing", "Instruction-level parallelism", "Out-of-order execution"],
        "templates": [
            ("Explain the role of {concept} in modern processors.", "It manages {concept} to ensure high throughput and correct architectural state."),
            ("How does {concept} handle pipeline hazards?", "By utilizing dynamic scheduling and tracking dependencies related to {concept}."),
            ("What are the performance implications of {concept}?", "It significantly reduces latency but increases hardware complexity and power consumption."),
            ("Describe a scenario where {concept} becomes a bottleneck.", "When the instruction window is saturated or memory latency exceeds the capacity of {concept}."),
            ("How is {concept} implemented in hardware?", "Typically using associative arrays, CAMs, and complex control logic tailored for {concept}."),
            ("Compare the use of {concept} in RISC vs CISC architectures.", "RISC relies heavily on compiler scheduling, whereas CISC hardware dynamically manages {concept}."),
            ("What happens to {concept} during a branch misprediction?", "The speculative state associated with {concept} is flushed to maintain correctness."),
            ("How does {concept} impact Average Memory Access Time (AMAT)?", "It hides latency, effectively reducing the penalty portion of the AMAT equation for {concept}."),
            ("Why is {concept} critical for multi-core scaling?", "It ensures that distributed resources remain synchronized and coherent regarding {concept}."),
            ("What are the power trade-offs of implementing {concept}?", "The dynamic power increases due to constant associative lookups required by {concept}.")
        ]
    },
    "Physical": {
        "concepts": ["Clock Tree Synthesis (CTS)", "Static IR Drop", "Dynamic IR Drop", "Electromigration (EM)", "Antenna Effect", "Useful Skew", "Clock Path Pessimism Removal (CPPR)", "On-Chip Variation (OCV)", "Gate-All-Around (GAA) transistors", "Decap insertion"],
        "templates": [
            ("How do you mitigate issues related to {concept} at 3nm nodes?", "By employing advanced DFM rules, redundant vias, and careful layer assignment for {concept}."),
            ("Explain the mathematical constraints governing {concept}.", "It relies on precise RC extraction and statistical variation models to bound {concept}."),
            ("What is the primary objective of {concept} during floorplanning?", "To minimize wirelength, balance loads, and ensure robust power delivery for {concept}."),
            ("How does {concept} affect setup and hold timing?", "It directly alters the arrival times at the capture flop, requiring careful balancing of {concept}."),
            ("Describe the physical mechanism behind {concept}.", "It is driven by parasitic capacitance, resistance, and extreme current densities in {concept}."),
            ("What EDA tools are used to analyze {concept}?", "Tools like RedHawk or Voltus perform dynamic simulations to sign-off on {concept}."),
            ("How do variable nanosheet widths impact {concept}?", "They change the drive strength and gate capacitance, complicating the analysis of {concept}."),
            ("Why are higher metal layers preferred when dealing with {concept}?", "Because they offer lower sheet resistance, which is critical for mitigating {concept}."),
            ("What is the role of dummy cells in preventing {concept}?", "They maintain uniform density, which is essential for CMP and reducing {concept}."),
            ("How does temperature inversion affect {concept}?", "At lower voltages, higher temperatures can actually speed up cells, flipping the worst-case corners for {concept}.")
        ]
    },
    "RTL": {
        "concepts": ["Asynchronous FIFOs", "Gray-code pointers", "Two-flop synchronizers", "Mealy state machines", "Moore state machines", "Round-robin arbiters", "AXI4 burst transactions", "VALID/READY handshakes", "Clock Domain Crossing (CDC)", "Reset synchronization"],
        "templates": [
            ("Design a robust mechanism for {concept}.", "Implement hardware that safely registers signals and avoids metastability using {concept}."),
            ("What are the corner cases when verifying {concept}?", "Handling back-to-back assertions, full/empty conditions, and asynchronous resets in {concept}."),
            ("Explain the difference between binary and {concept} encoding.", "{concept} ensures only one bit transitions at a time, preventing glitch propagation across domains."),
            ("How does {concept} prevent data loss across clock domains?", "By decoupling the read and write operations and safely passing pointers via {concept}."),
            ("Write the SystemVerilog assertions for {concept}.", "property p_concept; @(posedge clk) req |=> ##[1:$] ack; endproperty // tailored for {concept}"),
            ("What causes deadlock in {concept}?", "Circular dependencies or missing READY signals can halt {concept} indefinitely."),
            ("How do you optimize the critical path in {concept}?", "By pipelining the combinational logic and duplicating registers to reduce fan-out in {concept}."),
            ("Why is {concept} preferred over simple handshaking for high throughput?", "It allows continuous data streaming without waiting for round-trip acknowledgments, unlike basic {concept}."),
            ("Describe the state transitions in {concept}.", "The FSM moves from IDLE to ACTIVE, evaluating inputs to determine the next state of {concept}."),
            ("How do you handle unaligned transfers in {concept}?", "By utilizing byte strobes (WSTRB) and calculating the correct address offsets for {concept}.")
        ]
    },
    "Verification": {
        "concepts": ["UVM Scoreboards", "Constrained Random Verification", "Functional Coverage", "Code Coverage", "SystemVerilog Assertions (SVA)", "Formal Equivalence Checking", "ISO 26262 ASIL D", "Failure Modes and Effects Analysis (FMEA)", "Dual Core Lockstep", "Error-Correcting Code (ECC)"],
        "templates": [
            ("What is the primary function of {concept} in a testbench?", "To predict expected behavior and compare it against the actual DUT output for {concept}."),
            ("How do you achieve 100% {concept}?", "By writing targeted directed tests to hit corner cases missed by random stimulus in {concept}."),
            ("Explain the syntax and temporal operators used in {concept}.", "Using sequences, implications (|->), and repetition operators to define {concept}."),
            ("Why is {concept} insufficient for sign-off on its own?", "Because it only proves the code toggled, not that the architectural intent of {concept} was verified."),
            ("How does {concept} mathematically prove design correctness?", "By exploring the entire state-space without simulation vectors to verify {concept}."),
            ("What are the hardware overheads of implementing {concept}?", "It requires redundant logic, parity bits, and comparator circuits, increasing area for {concept}."),
            ("Describe the process of injecting faults to test {concept}.", "Using force/release statements or specialized UPF commands to simulate soft errors in {concept}."),
            ("How does {concept} handle systematic vs random hardware faults?", "Systematic faults are caught via rigorous DV, while random faults are mitigated by {concept}."),
            ("What is the role of the UVM Sequencer in relation to {concept}?", "It arbitrates and routes randomized transaction items to the driver for {concept}."),
            ("How do you resolve coverage holes in {concept}?", "By analyzing the coverage database and tweaking constraints to steer generation towards {concept}.")
        ]
    },
    "Software": {
        "concepts": ["Virtual Memory", "Demand Paging", "TLB Misses", "Memory Fragmentation", "C++ Virtual Functions", "Lock-free Data Structures", "Topological Sorting", "LRU Cache Implementation", "Mutexes and Semaphores", "Context Switching"],
        "templates": [
            ("How does the OS manage {concept}?", "By utilizing hardware page tables and handling page faults to abstract {concept}."),
            ("What is the performance overhead of {concept}?", "It induces pipeline stalls, cache trashing, and pipeline flushes associated with {concept}."),
            ("Implement an optimal algorithm for {concept}.", "Using a combination of HashMaps and Doubly Linked Lists to achieve O(1) time for {concept}."),
            ("How do you prevent race conditions when using {concept}?", "By utilizing atomic compare-and-swap (CAS) operations and memory barriers for {concept}."),
            ("Explain the hardware-software boundary for {concept}.", "The OS sets up the structures, but the MMU hardware traverses them during {concept}."),
            ("What causes a stack overflow in the context of {concept}?", "Infinite recursion or massive local allocations exceeding the thread's limit for {concept}."),
            ("How does {concept} impact instruction cache locality?", "Dynamic dispatch and jumping to arbitrary addresses ruin spatial locality in {concept}."),
            ("Describe the difference between user mode and kernel mode during {concept}.", "Kernel mode has unrestricted hardware access required to execute privileged {concept} instructions."),
            ("How do you resolve dependency graphs using {concept}?", "By calculating in-degrees and processing nodes using a queue, essential for {concept}."),
            ("Why is dynamic allocation avoided in embedded systems regarding {concept}?", "To prevent non-deterministic latency and catastrophic memory fragmentation in {concept}.")
        ]
    },
    "GPU_Execution": {
        "concepts": ["SIMT Architecture", "Warp Divergence", "Active Masks", "Dynamic Warp Scheduling", "Thread Block Occupancy", "Roofline Model", "Arithmetic Intensity", "Register Pressure", "Latency Hiding", "Instruction Serialization"],
        "templates": [
            ("How does {concept} differentiate GPUs from traditional CPUs?", "It allows thousands of threads to execute the same instruction stream, maximizing throughput via {concept}."),
            ("What happens to execution resources during {concept}?", "Execution is serialized, and idle threads consume cycles without doing useful work due to {concept}."),
            ("How do modern architectures mitigate the penalties of {concept}?", "By maintaining independent thread scheduling and per-thread program counters for {concept}."),
            ("Explain how to calculate {concept} for a given kernel.", "By dividing the total floating-point operations by the total bytes transferred from DRAM for {concept}."),
            ("What limits {concept} on a Streaming Multiprocessor (SM)?", "The physical limits of the register file and statically allocated shared memory bound {concept}."),
            ("How does {concept} influence whether a kernel is memory-bound?", "If the ratio falls below the machine balance point, the kernel is starved for data, reflecting {concept}."),
            ("Describe the mechanism of {concept} in hiding global memory latency.", "By rapidly context-switching to a different, ready warp while the stalled warp waits for {concept}."),
            ("Why does excessive {concept} lead to register spilling?", "When a thread demands too many registers, data spills to slow local memory, exacerbating {concept}."),
            ("How do synchronization barriers interact with {concept}?", "They force all threads in a block to reach a specific point, potentially stalling {concept}."),
            ("What is the impact of {concept} on power efficiency?", "High utilization is good, but thrashing and serialization waste dynamic power during {concept}.")
        ]
    },
    "Memory_Hierarchy": {
        "concepts": ["Shared Memory Bank Conflicts", "Global Memory Coalescing", "L2 Cache Misses", "HBM3 Bandwidth", "Memory Strides", "SASS Instruction Decomposition", "Memory Padding", "Wavefronts", "Thread Block Dimensions", "Scratchpad Memory"],
        "templates": [
            ("What is the root cause of {concept}?", "Multiple threads in a warp accessing different addresses that map to the same physical module causes {concept}."),
            ("How do you optimize a kernel to avoid {concept}?", "By adjusting access strides or adding dummy elements to shift the modulo mapping, preventing {concept}."),
            ("Explain the latency differences between registers and {concept}.", "Registers are 1 cycle, while {concept} can take hundreds of cycles if it misses the L1/L2 caches."),
            ("How does {concept} affect the effective memory bandwidth?", "It forces the memory controller to serialize requests, drastically reducing throughput due to {concept}."),
            ("Why is {concept} critical for saturating the memory bus?", "Because the bus transfers data in wide, aligned chunks (e.g., 32 bytes); unaligned accesses ruin {concept}."),
            ("Describe how {concept} impacts matrix transposition.", "Reading rows and writing columns naturally induces severe bank conflicts unless {concept} is managed."),
            ("What role does {concept} play in the Hopper architecture?", "It provides the massive 3TB/s+ bandwidth required to feed the Tensor Cores, defining {concept}."),
            ("How do 128-bit store instructions interact with {concept}?", "They are broken down at the SASS level into multiple transactions, which can trigger hidden {concept}."),
            ("Why is {concept} manually managed by the programmer unlike CPU caches?", "To provide deterministic, ultra-low latency access for cooperative thread data sharing via {concept}."),
            ("How does changing {concept} from 16x16 to 32x8 improve performance?", "It aligns the warp execution with the physical memory transaction size, optimizing {concept}.")
        ]
    },
    "Advanced_Accelerators": {
        "concepts": ["Tensor Cores", "Fused Multiply-Add (FMA)", "FP8 Precision", "Transformer Engine", "NVLink-C2C", "Hardware Cache Coherency", "NVSwitch Fabric", "Mixed-Precision Training", "Dynamic Scaling Factors", "Systolic Arrays"],
        "templates": [
            ("How do {concept} differ fundamentally from standard CUDA cores?", "They execute entire matrix operations (e.g., 4x4) in a single cycle rather than scalar operations, defining {concept}."),
            ("What is the primary advantage of using {concept} in LLM training?", "It halves the memory bandwidth requirement and doubles throughput without sacrificing accuracy via {concept}."),
            ("Explain how the hardware manages {concept} to prevent underflow.", "By analyzing tensor statistics and shifting the exponent bias dynamically during {concept}."),
            ("How does {concept} bridge the CPU and GPU memory spaces?", "It provides a 900 GB/s coherent interconnect, eliminating the need for slow PCIe DMA copies via {concept}."),
            ("Describe the architectural trade-offs of implementing {concept}.", "It requires massive crossbar routing and directory state tracking to maintain coherence across {concept}."),
            ("Why are {concept} essential for scaling beyond a single node?", "They allow up to 256 GPUs to communicate at full bandwidth as if they were on a single die using {concept}."),
            ("How does {concept} accelerate the attention mechanism?", "By rapidly computing the Q*K^T matrix multiplications at the hardware level using {concept}."),
            ("What are the physical design challenges of routing {concept}?", "Managing the extreme signal integrity and power delivery requirements of the high-speed SerDes for {concept}."),
            ("Explain the difference between software-managed migration and {concept}.", "Hardware coherence handles page faults and migrations transparently at the cache-line level for {concept}."),
            ("How does {concept} impact the thermal density of the die?", "The extreme switching activity of dense matrix math creates localized thermal hotspots requiring advanced cooling for {concept}.")
        ]
    },
    "Networking": {
        "concepts": ["Remote Direct Memory Access (RDMA)", "InfiniBand Protocol", "Queue Pairs (QP)", "Subnet Manager (SM)", "Credit-based Flow Control", "Virtual Lanes (VLs)", "Partition Keys (P_Keys)", "Zero-copy Networking", "Fat-tree Topologies", "Congestion Notification Packets"],
        "templates": [
            ("How does {concept} bypass the traditional TCP/IP stack?", "By allowing the network adapter to read/write directly to application memory, defining {concept}."),
            ("Explain the state transition machine required to initialize {concept}.", "It must progress strictly from RESET to INIT, RTR, and finally RTS to establish {concept}."),
            ("What happens if the {concept} fails in a large cluster?", "A standby manager must immediately take over to prevent routing loops and fabric collapse in {concept}."),
            ("How does {concept} guarantee lossless transmission?", "By ensuring a sender never transmits unless it has explicit buffer credits from the receiver for {concept}."),
            ("Why is {concept} used to prevent head-of-line blocking?", "It segregates traffic into independent logical channels on the same physical link using {concept}."),
            ("Describe how {concept} provides multi-tenant security.", "By enforcing hardware-level isolation, ensuring packets only route within the defined {concept}."),
            ("What is the latency advantage of {concept} over Ethernet?", "It achieves microsecond latencies by eliminating kernel context switches and CPU interrupts via {concept}."),
            ("How does {concept} calculate deterministic routing paths?", "By mapping the entire fabric topology and assigning unique Local Identifiers (LIDs) for {concept}."),
            ("Explain the role of {concept} in synchronous parallel training.", "It ensures that gradient all-reduce operations complete simultaneously across thousands of nodes via {concept}."),
            ("How do {concept} handle transient network congestion?", "By throttling specific flows at the source before buffers overflow, maintaining the lossless nature of {concept}.")
        ]
    },
    "Low_Power": {
        "concepts": ["Unified Power Format (UPF)", "Isolation Cells", "Level Shifters", "Retention Registers", "Integrated Clock Gating (ICG)", "Dynamic Voltage and Frequency Scaling (DVFS)", "Subthreshold Leakage", "Power Islands", "Multi-Vt Synthesis", "Dark Silicon"],
        "templates": [
            ("Why are {concept} mandatory when crossing power domains?", "To prevent floating inputs from causing massive short-circuit currents in the always-on domain via {concept}."),
            ("How does {concept} preserve state during deep sleep?", "By utilizing a secondary, always-on balloon latch to save the flop's value just before power-down in {concept}."),
            ("Explain the synthesis trade-offs when using {concept}.", "Faster LVT cells leak exponentially more power, so they are restricted only to the critical paths in {concept}."),
            ("What is the physical mechanism behind {concept}?", "As transistors shrink, the gate oxide becomes too thin to stop quantum tunneling, exacerbating {concept}."),
            ("How does {concept} reduce dynamic power consumption?", "By AND-ing the clock signal with an enable flag, preventing the clock tree from toggling idle logic via {concept}."),
            ("Describe the role of {concept} in modern SoC design.", "It separates the logical functionality from the physical power intent, allowing automated insertion of {concept}."),
            ("Why do we need {concept} between a 0.7V and 1.0V domain?", "To amplify the signal swing so the receiving logic correctly interprets the high/low thresholds via {concept}."),
            ("How does {concept} manage thermal limits?", "By dynamically lowering the voltage and clock speed when the chip approaches its thermal design power (TDP) using {concept}."),
            ("What are the verification challenges associated with {concept}?", "Ensuring that power-up/power-down sequences do not corrupt state or cause X-propagation in {concept}."),
            ("Explain the concept of {concept} in advanced nodes.", "The reality that we cannot power all transistors simultaneously due to thermal constraints, leading to {concept}.")
        ]
    }
}

questions = []
week_id = 1
for cat_name, cat_data in categories.items():
    for concept in cat_data["concepts"]:
        for template_q, template_a in cat_data["templates"]:
            q_text = template_q.format(concept=concept)
            a_text = template_a.format(concept=concept)
            questions.append({
                "type": cat_name.replace("_", " "),
                "q": q_text,
                "a": a_text,
                "weekId": f"w{week_id}",
                "weekN": week_id
            })
            week_id = (week_id % 48) + 1

# We have 10 categories * 10 concepts * 10 templates = 1000 questions.
# Let's save this to a json file.
with open("1000_questions.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Generated {len(questions)} questions.")
