from io import BytesIO
import base64
import matplotlib
matplotlib.use('agg')  # Use the 'agg' backend
import matplotlib.pyplot as plt

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):

    if chart_type == '#1':
        plt.figure(figsize=(10, 6))  # Set the figure size to avoid overlapping text
        bars = plt.bar(data['name'], data['difficulty_level_choices'], width=0.6)  # Adjust width as needed
        plt.xlabel('Recipe Name')
        plt.ylabel('Difficulty Level')
        plt.title('Difficulty Levels of Recipes')
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Adjust layout to prevent clipping
        plt.xlim(-0.5, len(data['name']) - 0.5)  # Set x-axis limits to include all bars

        for bar, difficulty_level in zip(bars, data['difficulty_level_choices']):
            if difficulty_level == 'easy':
                bar.set_color('skyblue')  # Change color for better visibility
                bar.set_linewidth(20)  # Set the bar border width
                bar.set_edgecolor('blue')  # Set the bar border color
                bar.set_alpha(0.7)  # Adjust transparency if needed
            if difficulty_level == 'medium':
                bar.set_color('green')  # Change color for better visibility
                bar.set_linewidth(2)  # Set the bar border width
                bar.set_edgecolor('green')  # Set the bar border color
                bar.set_alpha(0.7)  # Adjust transparency if needed
            if difficulty_level == 'hard':
                bar.set_color('red')  # Change color for better visibility
                bar.set_linewidth(2)  # Set the bar border width
                bar.set_edgecolor('red')  # Set the bar border color
                bar.set_alpha(0.7)  # Adjust transparency if needed
    elif chart_type == '#2':
        labels = data['category_choices']
        category_counts = {category: data['category_choices'].count(category) for category in labels}
        plt.figure(figsize=(10, 6))  # Set the figure size
        plt.pie(category_counts.values(), labels=category_counts.keys(), autopct='%1.1f%%')
        plt.title('Percentage of Recipes by Category')  # Add a title
    elif chart_type == '#3':
        plt.figure(figsize=(10, 6))  # Set the figure size
        plt.plot(data['name'], data['cooking_time'])
        plt.xlabel('Recipe Name')
        plt.ylabel('Cooking Time')
        plt.title('Cooking Time of Recipes')
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
        plt.tight_layout()  # Adjust layout to prevent clipping
    else:
        return None

    # Save chart to bytes buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Encode image to base64
    return base64.b64encode(buf.read()).decode('utf-8')
