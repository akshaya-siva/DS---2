import matplotlib.pyplot as plt
import streamlit as st

def plot_metrics_chart(metrics, models):
    """
    Plots a bar chart for model performance metrics.
    
    Args:
        metrics (dict): A dictionary containing metric names as keys and a list of values for each model.
        models (list): A list of model names corresponding to the metrics.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for metric_name, values in metrics.items():
        ax.bar(models, values, label=metric_name)
    
    ax.set_title("Model Performance Metrics")
    ax.set_ylabel("Score")
    ax.legend()
    
    st.pyplot(fig)

def plot_comparison_chart(metrics_before_tuning, metrics_after_tuning, models):
    """
    Plots a comparison chart showing before and after fine-tuning metrics.
    
    Args:
        metrics_before_tuning (dict): Metrics before fine-tuning.
        metrics_after_tuning (dict): Metrics after fine-tuning.
        models (list): A list of model names.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    x = range(len(models))
    
    for metric_name in metrics_before_tuning.keys():
        ax.plot(x, metrics_before_tuning[metric_name], marker='o', label=f"{metric_name} (Before)")
        ax.plot(x, metrics_after_tuning[metric_name], marker='x', linestyle='--', label=f"{metric_name} (After)")
    
    ax.set_xticks(x)
    ax.set_xticklabels(models)
    
    ax.set_title("Comparison of Metrics Before and After Fine-Tuning")
    ax.set_ylabel("Score")
    ax.legend()
    
    st.pyplot(fig)
