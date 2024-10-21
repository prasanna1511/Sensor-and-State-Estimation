
### Algorithm: Odometry Motion Model

#### Input:
- `prev_pose` = (x, y, θ) → Previous robot pose
- `cur_pose` = (x', y', θ') → Current robot pose
- `odom` = (Δrot1, Δtrans, Δrot2) → Odometry readings (control input)
- `alpha` = (α1, α2, α3, α4) → Noise parameters for motion uncertainty

#### Output:
- Posterior probability `p(x'|x, u)` → Likelihood of transitioning from `prev_pose` to `cur_pose` given odometry readings.

---

#### 1. **Calculate Odometry-Based Motion**:
   - **Translation:**
     ```math
     Δtrans = \sqrt{(x' - x)^2 + (y' - y)^2}
     ```

   - **First Rotation (Δrot1):**
     ```math
     Δrot1 = \text{atan2}(y' - y, x' - x) - θ
     ```
     - rotation angle needed to align with the direction of movement from the previous pose.

   - **Second Rotation (Δrot2):**
     ```math
     Δrot2 = θ' - θ - Δrot1
     ```
     - final rotation to align with the new orientation.
---
#### 2. **Motion Uncertainty (Noise Model)**:
   - Introduce random Gaussian noise based on motion. This models real-world uncertainty in robot movements.

   - **Probabilities** (Gaussian Noise Model):
     - **p1**: Likelihood of the first rotation given noise:
       ```math
       p1 = \text{prob}(\hat{Δrot1} - Δrot1, \alpha1 \cdot |Δrot1| + \alpha2 \cdot |Δtrans|)
       ```
     - **p2**: Likelihood of the translation given noise:
       ```math
       p2 = \text{prob}(\hat{Δtrans} - Δtrans, \alpha3 \cdot |Δtrans| + \alpha4 \cdot (|Δrot1| + |Δrot2|))
       ```
     - **p3**: Likelihood of the second rotation given noise:
       ```math
       p3 = \text{prob}(\hat{Δrot2} - Δrot2, \alpha1 \cdot |Δrot2| + \alpha2 \cdot |Δtrans|)
       ```
---
#### 3. **Posterior Probability**:
   - Combine the three probabilities to get the overall likelihood of the motion:
     ```math
     p(x' | x, u) = p1 \cdot p2 \cdot p3
     ```
---
#### 4. **Sampling for Motion**:
   - To simulate the motion with noise, use random samples based on noise parameters:
     - **Sample for Δrot1**:
       ```math
       \hat{Δrot1} = Δrot1 + \frac{1}{2} \sum_{i=1}^{12} \text{rand}(-b, b)
       ```
     - **Sample for Δtrans**:
       ```math
       \hat{Δtrans} = Δtrans + \frac{1}{2} \sum_{i=1}^{12} \text{rand}(-b, b)
       ```
     - **Sample for Δrot2**:
       ```math
       \hat{Δrot2} = Δrot2 + \frac{1}{2} \sum_{i=1}^{12} \text{rand}(-b, b)
       ```
---
#### 5. **Update Pose (x', y', θ')**:
   - Compute the new pose based on sampled motion:
     - **New x-coordinate**:
       ```math
       x' = x + \hat{Δtrans} \cdot \cos(θ + \hat{Δrot1})
       ```
     - **New y-coordinate**:
       ```math
       y' = y + \hat{Δtrans} \cdot \sin(θ + \hat{Δrot1})
       ```
     - **New orientation**:
       ```math
       θ' = θ + \hat{Δrot1} + \hat{Δrot2}
       ```

---

Robot movementfrom one pose to another using odometry (control inputs). It accounts for uncertainties (noise) in the movement through a probabilistic model and sampling. The final output is the updated pose (`x', y', θ'`) and the posterior probability (`p(x'|x, u)`) representing the likelihood of the motion given the inputs.
