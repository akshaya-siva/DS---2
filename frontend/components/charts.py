import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def plot_metrics_chart(metrics):
    """
    Plots a bar chart for class-wise metrics (Class 0 vs Class 1).
    
    Args:
      metrics (dict): Dictionary with metric names as keys and values for each class
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Safely extract values for each class
    class_0_values = []
    class_1_values = []
    metric_names = list(metrics.keys())
    
    for metric, value in metrics.items():
        if isinstance(value, list):
            # If value is a list, take first element for Class 0
            class_0_values.append(value[0])
            # Only take second element for Class 1 if it exists
            class_1_values.append(value[1] if len(value) > 1 else 0)
        else:
            # If value is not a list, assign it to Class 0 only
            class_0_values.append(value)
            class_1_values.append(0)
    
    # Bar positions
    x = np.arange(len(metric_names))
    width = 0.35
    
    # Create bars with colors matching the image
    ax.bar(x - width/2, class_0_values, width, label='Class 0', color='#26c6da')
    ax.bar(x + width/2, class_1_values, width, label='Class 1', color='#ffcc80')
    
    # Add styling
    ax.set_ylabel('Score')
    ax.set_title('Class-wise Performance Metrics')
    ax.set_xticks(x)
    ax.set_xticklabels(metric_names)
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Set y-axis limits to match the image
    ax.set_ylim(0, 1.05)
    
    # Display in Streamlit
    st.pyplot(fig)

def plot_comparison_chart(metrics_default, metrics_tuned):
    """
    Plots a comparison chart showing default vs tuned model metrics.
    
    Args:
        metrics_default (dict): Metrics for default model
        metrics_tuned (dict): Metrics for tuned model
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Extract metrics that exist in both dictionaries
    common_metrics = [m for m in metrics_default.keys() if m in metrics_tuned]
    
    # For each metric, extract values for comparison
    for metric in common_metrics:
        # Default model values
        default_class0 = metrics_default[metric][0] if isinstance(metrics_default[metric], list) else metrics_default[metric]
        default_class1 = metrics_default[metric][1] if isinstance(metrics_default[metric], list) and len(metrics_default[metric]) > 1 else 0
        
        # Tuned model values
        tuned_class0 = metrics_tuned[metric][0] if isinstance(metrics_tuned[metric], list) else metrics_tuned[metric]
        tuned_class1 = metrics_tuned[metric][1] if isinstance(metrics_tuned[metric], list) and len(metrics_tuned[metric]) > 1 else 0
        
        # Set up x positions
        x = np.arange(len(common_metrics))
        width = 0.2
        
        # Create grouped bars for comparison
        ax.bar(x - width*1.5, [default_class0], width, label='Default Class 0', color='#26c6da')
        ax.bar(x - width*0.5, [default_class1], width, label='Default Class 1', color='#80deea')
        ax.bar(x + width*0.5, [tuned_class0], width, label='Tuned Class 0', color='#ffcc80')
        ax.bar(x + width*1.5, [tuned_class1], width, label='Tuned Class 1', color='#ffb74d')
    
    # Add styling
    ax.set_ylabel('Score')
    ax.set_title('Comparison of Default vs Tuned Model Performance')
    ax.set_xticks(x)
    ax.set_xticklabels(common_metrics)
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Display in Streamlit
    st.pyplot(fig)
