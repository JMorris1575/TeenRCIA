=================================
Design Ideas for TeenRCIA Website
=================================

The idea is to create a convenient place for teen RCIA catechumens to interact with the pastor, RCIA leaders, their
sponsors and one another. Various activities will be posted, such as links to videos and associated discussion areas.

I have today (1-13-2019) discovered that it needs to be called Youth RCIA instead of Teen RCIA. One of my future
catechumens is only 11.

Narrative Walkthrough
=====================

Fred Flintstone, a St. Basil teen RCIA catechumen, comes to the website and logs in with the credentials he received in
e-mail. After logging in he finds himself on the welcome page with a list of the activities that have been posted so
far. Some are marked "Begin" if Fred has not yet participated in any way, others are marked "Continue" if Fred has
contributed, while others are marked "Review Only" if that activity is old enough or far enough back in the sequence to
not matter anymore. After a time, activities can be moved to an archive page. This is Fred's first time to the website
and there is only one activity listed. He clicks on it and comes to the corresponding activity page.

The first thing he notices is that, on the left hand side of the page, there is an image related to Saint Basil the
Great, offering an inspirational quote. He looks at the image and the quote and either ignores it, or sees that it has
an application to his life. The next time he visits an activity page there will probably be a different image there as
they are assigned randomly from a list.

On the right hand side of the page he finds an overview for the activity and a list of sections he is to complete,
perhaps with an idea of when it should be completed. Clicking on a section button will bring him to the page for
that section. At the bottom of the instructions is a "Return to Welcome Page" button that, you guessed it, returns him
to the Welcome page with its activity list.

Each section page will have some instructions on what Fred is to do, often including a link or links to Chosen videos,
and a series of discussion points or questions to which he, and the others, will respond. Some discussions can be
continuous by design if you can think of the right type of question. Depending on the item in question, Fred can respond
to questions, comment on the videos or, in general, participate in a discussion. He can edit or delete his own posts but
only view the posts made by other members of the group. As the website develops, perhaps he can make comments to
particular entries by other members of the group. At the bottom of the section page there will be buttons to return to
the activity page or to the welcome page. (The St. Basil icon or Website title in the header are also links to return to
the Welcome page.)

As time goes on Fred will find activities posted quite frequently and will be encouraged to check the website daily and
add something to it.

First Thoughts on Design
========================

So far I only sense the need for one app, the activity app, since, as currently designed, there is only one kind of page
aside from the Welcome page, and that is the activity page. The activity page allows for discussion and they will all be
open discussions. Here are some first thoughts on Model design:

Activity Model:

#. index (an integer indicating the order in which this activity should appear)
#. overview (a char field giving an overview of the whole activity to appear in the instruction box.)
#. publish date (the date on which it is to first appear)
#. open (a boolean field indicating whether this activity is still open for discussion or only review)
#. archive (a boolean field indicating whether this activity should appear only on the archive page)

Section Model:

#. index (an integer indicating the order in which this section should appear in the activity's section list)
#. activity (foreign key to the activity to which this section belongs)
#. instructions (char field for the instructions)
#. link (link to a video or other resource to spur discussion)

Item Model:

#. index (an integer indicating the order in which this item should appear.
#. section (foreign key to the section to which this item belongs)
#. text (char field for the prompt or question text)

Post Model:

#. user (foreign key to the user making this post)
#. text (text field for the contents of the post)
#. post_date_time (date_time field for this post - and the order in which it will be displayed)

Comment Model:

#. post (foreign key to the post to which this comment belongs)
#. text (text field for the contents of this comment)
#. comment_date_time (date_time field for this comment - and the order in which it will be displayed)

Overall URL Scheme
==================

+---------------------------------+----------------------------------------------------------------------------------+
| URL                             | Destination                                                                      |
+=================================+==================================================================================+
| ``/``                           | redirects to login page if they are not logged in, welcome page otherwise        |
+---------------------------------+----------------------------------------------------------------------------------+
| ``login/``                      | login page                                                                       |
+---------------------------------+----------------------------------------------------------------------------------+
| ``logout/``                     | logout page                                                                      |
+---------------------------------+----------------------------------------------------------------------------------+
| ``activity/welcome``            | Summary page that lists all of the activities                                    |
+---------------------------------+----------------------------------------------------------------------------------+
| ``activity/<a>/``               | Summary page for activity <a> giving its overview and a list of active sections  |
+---------------------------------+----------------------------------------------------------------------------------+
| ``activity/<a>/<n>/``           | Section page for section n of activity a                                         |
+---------------------------------+----------------------------------------------------------------------------------+
| ``activity/create/<a>/<n>/<t>`` | Page to create post or comment (indciated by t) for activity a and section n     |
+---------------------------------+----------------------------------------------------------------------------------+
| ``activity/edit/<t>/<pk>/``     | Edit page for text for either post or comment <pk> indicated by <t>              |
+---------------------------------+----------------------------------------------------------------------------------+
| ``activity/delete/<t>/<pk>/``   | Deletion confirmation page for either post or comment <pk> indicated by <t>      |
+---------------------------------+----------------------------------------------------------------------------------+
