#!/usr/bin/env python3
import bs4like

"""
READ THIS!

In this exercise you will operate on a tree of tags, which simulates the
BeautifulSoup4 interface, but is limited on purpose to only the most basic
tree walking operations.

IMPORTANT: There are no text nodes (all were removed), so you can ignore them.

For each tag/soup you have only these attributes available:

  tag.name - name of the tag
  tag.contents - list of children tags
  tag.parent - parent tag
  tag.next_sibling - next sibling tag
  tag.previous_sibling - previous sibling tag

You can additionally:

  print(tag) - to see the tag and its subtree as HTML
  tag.secret() - retrieve the secret from the tag

Solve the 4 exercises below (exercise_A, exercise_B, exercise_C, exercise_D) to
get the 4 secrets, which will decrypt the flag (see the code at the bottom).
"""


def exercise_A():
  """
  The HTML structure is as follows:
  <html>  <----------------------------------------------- you start here
    <head></head>
    <body>
      <h1></h1>
      <div>
        <p></p>
        <p></p>
      </div>
      <div>
        <p></p>
        <p></p>
        <p SECRET-IS-HERE-CALL-.secret()-ON-ME></p>  <---- you need to get here
      </div>
      <div>
        <p></p>
        <p></p>
      </div>
    </body>
  </html>
  """

  soup = bs4like.exercise_A()

  # Your code goes here.

  return None  # Replace with return destination_tag.secret()


def exercise_B():
  """
  Similar to exercise A, but you start in a different place, and the secret
  moved slightly.

  IMPORTANT: There are no text nodes (all were removed), so you can ignore them.

  The HTML structure is as follows:
  <html>
    <head></head>
    <body>
      <h1></h1>
      <div>
        <p></p>
        <p SECRET-IS-HERE-CALL-.secret()-ON-ME></p>  <---- you need to get here
      </div>
      <div>
        <p></p>
        <p></p>
        <p></p>
      </div>
      <div>
        <p></p> <----------------------------------------------- you start here
        <p></p>
      </div>
    </body>
  </html>
  """

  tag = bs4like.exercise_B()

  # Your code goes here.

  return None  # Replace with return destination_tag.secret()


def exercise_C():
  """
  Something a bit more fun!

  IMPORTANT: There are no text nodes (all were removed), so you can ignore them.

  The HTML structure is as follows:
  <html>
    <head>
      <title></title>
      <meta></meta>
      <meta></meta>
      <meta></meta>
      <meta></meta>
      <link></link>
      <link></link>
      <script></script>
      <script></script>
    </head>
    <body>
      <div>
        <div>
          <header>
            <div>
              <p>
                <b></b>
                <i></i>
                <span></span> <--------------------------------- you start here
              </p>
              <div>
                <img></img>
                <span></span>
              </div>
            </div>
          </header>
          <div>
            <div>
              <p></p>
              <p></p>
              <p></p>
              <p>
                <b></b>
                <i></i>
                <span></span>
              </p>
              <p>
                <b></b>
                <i></i>
                <span></span>
              </p>
            </div>
          </div>
          <div>
            <div>
              <p></p>
              <ul>
                <li></li>
                <li SECRET-IS-HERE-CALL-.secret()-ON-ME></li> <------- get here
              </ul>
            </div>
          </div>
        </div>
        <footer>
          <div>
            <div>
              <p></p>
              <p></p>
            </div>
          </div>
        </footer>
      </div>
    </body>
    <script></script>
  </html>
  """

  tag = bs4like.exercise_C()

  # Your code goes here.

  return None  # Replace with return destination_tag.secret()


def exercise_D():
  """
  Similar to exercise C, but you start in a different place, and the secret
  moved slightly.

  IMPORTANT: There are no text nodes (all were removed), so you can ignore them.

  The HTML structure is as follows:
  <html>
    <head>
      <title></title>
      <meta></meta>
      <meta></meta>
      <meta></meta>
      <meta></meta>
      <link></link>
      <link></link>
      <script></script>
      <script SECRET-IS-HERE-CALL-.secret()-ON-ME></script> <--------- get here
    </head>
    <body>
      <div>
        <div>
          <header>
            <div>
              <p>
                <b></b>
                <i></i>
                <span></span>
              </p>
              <div>
                <img></img>
                <span></span>
              </div>
            </div>
          </header>
          <div>
            <div>
              <p></p>
              <p></p>
              <p></p>
              <p>
                <b></b>
                <i></i>
                <span></span>
              </p>
              <p>
                <b></b>
                <i></i> <--------------------------------------- you start here
                <span></span>
              </p>
            </div>
          </div>
          <div>
            <div>
              <p></p>
              <ul>
                <li></li>
                <li></li>
              </ul>
            </div>
          </div>
        </div>
        <footer>
          <div>
            <div>
              <p></p>
              <p></p>
            </div>
          </div>
        </footer>
      </div>
    </body>
    <script></script>
  </html>
  """

  tag = bs4like.exercise_D()

  # Your code goes here.

  return None  # Replace with return destination_tag.secret()

# Call the exercises, get the secrets, and decrypt the flag.
secret1 = exercise_A()
secret2 = exercise_B()
secret3 = exercise_C()
secret4 = exercise_D()
bs4like.print_decrypted_flag(secret1, secret2, secret3, secret4)