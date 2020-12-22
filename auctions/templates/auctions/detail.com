{% extends "auctions/layout.html" %}

{% block body %}
    <h1> List </h1>
   {{ show.image.url }}
   <h3>This Item is Posted by: <span Style="color: blue;">{{data.posted_by}}</span></h3>

{% if data %}
   <div>
          <div class="column">
               <a href="{% url 'addwatchlist' data.id %}"><button class="btn btn-primary">Add to watchlist</button></a>
          </div>
          <div class="column">
          	{% endif %}
              
               {% if user.username %}
               {% if data.posted_by %}
               <br>
                  <a href="{% url 'closed' data.id%}"><button class="btn btn-warning">Close Bid</button></a>
             <br>
             		{% endif %}
             	{% endif %}
             
               
               
          </div>
    </div>
          <br></br>
    <div>
          <div class="column">
               {% if data.image %}
                   <img src="{{ data.image.url }}" height="300" width="300">
               {% else %}
                   <h3>Image not available.</h3>
               {% endif %}
          </div>
          <div class="column">
              <h3>Title: {{ data.title }}</h3>
              <h3>Starting Bid in $: {{ data.starting_bid }}</h3>
              <h3>Description: {{ data.description }}</h3>
              <h3>Category: {{ data.category }}</h3>
              <h3>Created_Date: {{ data.date_posted }}</h3>
              {% if bd.bid >= data.starting_bid %}
               <h2  Style="color: green;">Current Bid:${{bd.bid}}</h2>
           {% else %}
           <h4 Style="color: red;"> Please make a Bid higher than the Starting Bid!!! </h4>
           {% endif %}
           </div>
      </div>
          <br></br>
          <h2 Style="font-weight: bold; color: #A52A2A;"> Place your Bid here: 
          {% if data %}
         <form action="{% url 'bid_new' data.id %}" method="post">
            {% csrf_token%}
            <input type="number" name="bid">
             <input type="submit">
             	</form>
             {% endif %}
          <br></br>
          <h2 Style="font-weight: bold; color: blue;">Please Write your Comments here:</h2>
              {% if data %}
              	 <form action="{% url 'comnt' data.id %}" method="post">
                   {% csrf_token %}
                   
                   <textarea type="text" name="message"></textarea>
                   
                   <input type="submit">
               </form>
                  {% endif %}
                <br></br>
               
               <h2 Style="font-weight: bold; color: #008080;">Comments:</h2>
               
               {% for comments in c %}
               <ul>
                  
                 <li> <span class="card-title"><h3 Style="color: #DC143C;">{{comments.user_id}}</h3> <h3 Style="color: #000000;">Comment: {{comments.message}}</h3></span>
                 </li>
                  
               </ul>
               {% endfor %}
               
                
{% endblock %}
   
   
   
   
