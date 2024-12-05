# **FluxWallet: A Decentralized, Immutable Wallet Framework**

**Author**: Callum Maystone  
**Date**: December 2024  
**Location**: Adelaide, Australia

---

## **Abstract**
FluxWallet is a transformative approach to decentralized wallet systems, combining hierarchical structures, GitHub OAuth authentication, and a robust validation framework to create a secure, tamper-proof, and user-controlled repository for digital assets and data. By leveraging known truths, immutable data storage, and self-contained wallet systems, FluxWallet offers a revolutionary way for users to own, manage, and expand their digital presence securely.

---

## **1. Introduction**
In an era where decentralization and user autonomy are paramount, FluxWallet emerges as a solution that marries simplicity with security. Built on the foundations of GitHub repositories and leveraging OAuth as the backbone for authentication, FluxWallet transforms traditional wallet concepts into a **self-contained, forkable system** that users own entirely.

By introducing innovative mechanisms like **4D DNS**, **state validation**, and **token-driven encryption**, FluxWallet ensures data integrity, decentralization, and extensibility, all while providing a seamless user experience.

---

## **2. Key Concepts and Journey**
### **2.1 The Problem**
Existing wallet systems often rely on centralized servers, exposing them to vulnerabilities such as:
- Single points of failure.
- Data tampering.
- Limited user control and flexibility.

### **2.2 The Solution**
FluxWallet decentralizes wallet storage by:
- Treating each wallet as a **GitHub repository**.
- Securing data through **OAuth tokens** as encryption and validation keys.
- Implementing hierarchical structures and **4D DNS** for logical organization.

### **2.3 The Journey**
The FluxWallet concept evolved from:
1. The need for **self-sovereign identity and control**.
2. Inspiration from decentralized principles (e.g., blockchain, Satoshi Nakamoto).
3. The desire to build a lightweight, extensible system accessible to everyone.

---

## **3. Technical Foundations**
### **3.1 GitHub OAuth Integration**
GitHub OAuth is the core authentication mechanism, offering:
- **User Verification**: Tokens tied to GitHub accounts ensure authenticity.
- **Encryption Key**: Tokens double as keys for encrypting wallet data.
- **Decentralized Control**: Users manage their wallets directly through their GitHub accounts.

### **3.2 4D DNS**
FluxWallet introduces a **four-dimensional DNS system** for addressing wallets and nodes:
- **Format**: `XYZ.XYZ.XYZ.XYZ` (e.g., `node0.node1.node2.node3`).
- **Purpose**:
  - Encodes relationships and locations within the wallet structure.
  - Stores metadata for validation and traversal.

### **3.3 State Validation**
FluxWallet validates data changes through:
- **Token TTL and Time Sync**:
  - Ensures tokens are fresh by checking their TTL.
  - Synchronizes time between local machines and GitHub servers.
- **Known Truths**:
  - Uses anchors like `8.8.8.8` (Google DNS) for global validation.

---

## **4. Architecture**
### **4.1 Wallet Structure**
Each wallet is a self-contained GitHub repository containing:
- **JSON Files**:
  - Store state changes and hierarchical relationships.
- **Encryption Keys**:
  - Derived from OAuth tokens.
- **Validation Scripts**:
  - Automate state checks and ensure data integrity.

### **4.2 Hierarchical Relationships**
Nodes are structured logically:
- **Root Node** (`n0`): The genesis node of the wallet.
- **Child Nodes** (`n1`, `n2`, etc.): Subdivisions of the root.
- **Traversal**: Paths like `n1/n0`, `n2/n0` represent hierarchical relationships, akin to folder structures.

### **4.3 Transaction Flow**
1. **Initiation**: User sends data/transaction via their wallet.
2. **Validation**:
   - Checks token authenticity.
   - Validates state changes against known truths.
3. **Completion**: Data is encrypted and stored in the repository.

---

## **5. Features and Innovation**
### **5.1 Decentralization**
- **User-Owned Repos**: Each wallet is forked and maintained by the user.
- **Public/Private Control**: Wallets can be public or private based on user preference.

### **5.2 Immutability**
- **State Changes**: Wallet data is immutable, with every change validated and logged.
- **Known Truths**: Validation against global anchors ensures consistency.

### **5.3 Extensibility**
- **Forkable Tools**: Users can build and integrate custom tools.
- **Community Collaboration**: Encourages open-source development.

---

## **6. Use Cases**
### **6.1 Personal Wallets**
- Secure storage for digital assets and data.
- Tamper-proof transaction logs.

### **6.2 Knowledge Networks**
- Store and validate decentralized knowledge contributions.
- Reward contributors with tokens.

### **6.3 Transparent Validation**
- Publicly auditable wallets for organizations.
- Immutable records for compliance and accountability.

---

## **7. Roadmap**
### **Phase 1: Core Wallet Functionality**
- Implement encryption and validation modules.
- Build the wallet structure.

### **Phase 2: 4D DNS and Tooling**
- Introduce hierarchical addressing.
- Develop a suite of tools for wallet interaction.

### **Phase 3: Community Engagement**
- Launch community-driven initiatives.
- Introduce tokenized rewards for contributors.

---

## **8. Conclusion**
FluxWallet represents a paradigm shift in digital wallets, combining decentralization, security, and user control. By leveraging GitHub OAuth, 4D DNS, and hierarchical relationships, it provides a robust foundation for the future of decentralized data and asset management.

---

## **Appendix**
### **A. Known Truths**
Examples of global validation anchors:
- `8.8.8.8` (Google DNS).
- GitHub’s OAuth token issuance.

### **B. Sample Wallet Structure**
```plaintext
FluxWallet/
  |- wallet.json
  |- state_changes.json
  |- keys/
      |- encryption_key.pem
  |- scripts/
      |- validate.py
      |- encrypt.py
```

### **C. Token Validation Script**
```python
import time

def validate_token(token, ttl, server_time):
    current_time = time.time()
    creation_time = current_time - ttl
    if abs(server_time - current_time) > 5:
        raise Exception("Time sync error")
    return True
```

---

FluxWallet: Decentralized wallets, reimagined for the future.

