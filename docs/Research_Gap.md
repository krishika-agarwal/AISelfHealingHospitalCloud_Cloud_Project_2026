# Research Gaps (Ppaer wise)

1. Adaptive anomaly detection has been explored successfully, but identifying an anomaly and understanding the actual reason behind it are still separate issues. The study also does not examine how this type of adaptive detection would perform in cloud infrastructure supporting Hospital Information Systems.

2. The study connects graph-based anomaly detection with resource reallocation, but detailed explainability and adaptive remediation are not explored together. Its performance in healthcare-specific cloud infrastructure is also not evaluated.

3. Accurate anomaly prediction does not automatically provide information about why the anomaly is expected to occur or which component is responsible for it. Explainability and root-cause localisation therefore remain important gaps alongside anomaly prediction.

4. High anomaly detection performance is achieved using a complex combination of graph, temporal and generative models, but interpreting the reason behind individual anomaly decisions remains difficult. The connection between this type of advanced anomaly detection and subsequent recovery actions is also not addressed.

5. The method can identify a likely faulty service, but it provides less information about the exact monitoring features or conditions responsible for that failure. There is therefore still a gap between service-level root-cause identification, detailed explanation and post-diagnosis recovery.

6. Temporal causal analysis improves root-cause identification, but diagnosis and automated recovery remain separate processes. There is also limited evidence regarding the use of this type of causal RCA for cloud infrastructure supporting Hospital Information Systems.

7. The paper demonstrates that an AI agent can perform autonomous cloud fault mitigation, but broader validation and structured explanation of the agent's decisions remain limited. These issues become especially important when autonomous actions are considered for critical cloud environments.

8. Although prediction and automated remediation are considered together, the reasoning connecting monitored cloud conditions, failure predictions and selected remediation actions is not clearly explained. Detailed experimental validation and healthcare-specific evaluation also remain limited.

9. Current XAI-based anomaly detection research does not provide a reliable mechanism to determine whether generated explanations truly represent the underlying cause of an anomaly. This limitation becomes more significant in cloud infrastructure environments where formal ground truth cannot be established.

10. Existing contextual anomaly detection methods based on Quantile Regression Forests are not designed for streaming environments. This limits their usefulness for cloud infrastructure, where system metrics are generated continuously and require real-time analysis.

11. Although the proposed workflow successfully performs detection, explanation, and classification, it does not support automated response or recovery after an anomaly has been identified. As a result, the process remains dependent on manual decision-making.

12. The proposed framework assumes that the underlying cloud infrastructure continues to operate reliably without considering how changes in system behaviour or infrastructure failures would be detected and managed over time.

13. Although the study discusses limitations related to performance, privacy, and cost, it does not explore intelligent mechanisms for continuously monitoring cloud infrastructure or managing system reliability automatically. As a result, the role of AI-driven operational management remains largely unexplored.

14. Although the study identifies security concerns, limited technical expertise, and staffing shortages as major barriers to cloud adoption, it does not investigate how intelligent automation or AI-based operational support could help address these challenges.

15. The study recognizes the importance of monitoring in serverless healthcare systems but does not describe the processes involved in anomaly detection, explanation, or automated recovery. As a result, monitoring remains a conceptual component rather than an intelligent operational mechanism.