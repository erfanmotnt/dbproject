import React, { useState, useEffect, Component } from 'react';
import {
  Button,
  Form,
  Grid,
  Header,
  Message,
  Segment,
  Container,
  Dropdown,
} from 'semantic-ui-react';
import { Link } from 'react-router-dom';
import { createAccount } from '../redux/actions/account';
import { connect, useStore } from 'react-redux';



const CreateAccount = ({ isFetching, createAccount }) => {
  const [username, setUsername] = useState();
  const [firstName, setFirstName] = useState();
  const [lastName, setLastName] = useState();
  const [phone, setPhone] = useState();
  const [email, setEmail] = useState();
  const [role, setRole] = useState('w');

  async function handleSubmit(event) {
    const ok = isFormDataOk()
    if (ok) {
      createAccount(username, firstName, lastName, phone, email, role);
    }
  }

  function isFormDataOk() {
    return true //todo: validate data
  }

  return (
    <Container>
      <Grid centered doubling container stackable>
        <Grid.Row verticalAlign='middle'>
          <Grid.Column
            textAlign='center'
            width={6}
          >
            <Header as="h2" textAlign="center">
              ساخت حساب
            </Header>

            <Segment>
              <Form
                size="large"
                onSubmit={handleSubmit}
                loading={isFetching}
              >
                <Form.Input
                  name="username"
                  required
                  fluid
                  placeholder="نام کاربری"
                  className="persian-input"
                  value={username}
                  onChange={(event) => setUsername(event.target.value)}
                >
                  <input style={{ direction: 'ltr' }} />
                </Form.Input>

                <Form.Input
                  name="firstName"
                  type="name"
                  required
                  fluid
                  placeholder="نام"
                  className="persian-input"
                  value={firstName}
                  onChange={(event) => setFirstName(event.target.value)}
                >
                  <input style={{ direction: 'rtl', textAlign: 'right' }} />
                </Form.Input>

                <Form.Input
                  name="lastName"
                  type="name"
                  required
                  fluid
                  placeholder="نام خانوادگی"
                  className="persian-input"
                  value={lastName}
                  onChange={(event) => setLastName(event.target.value)}
                >
                  <input style={{ direction: 'rtl', textAlign: 'right' }} />
                </Form.Input>

                <Form.Input
                  name="phoneNumber"
                  type="phone"
                  required
                  fluid
                  placeholder="شماره‌موبایل"
                  className="persian-input"
                  value={phone}
                  onChange={(event) => setPhone(event.target.value)}
                >
                  <input style={{ direction: 'ltr' }} />
                </Form.Input>

                <Form.Input
                  name="email"
                  type="mail"
                  required
                  fluid
                  placeholder="ایمیل"
                  className="persian-input"
                  value={email}
                  onChange={(event) => setEmail(event.target.value)}
                >
                  <input style={{ direction: 'ltr' }} />
                </Form.Input>

                <Form.Input >
                  <Dropdown
                    style={{ direction: 'rtl', textAlign: '-webkit-right' }}
                    placeholder='انتخاب نوع حساب کاربری'
                    fluid
                    selection
                    options={[
                      {
                        key: '1',
                        text: 'مدرس',
                        value: 'teacher',
                      },
                      {
                        key: '2',
                        text: 'منتور',
                        value: 'mentor',
                      },
                      {
                        key: '3',
                        text: 'مدیر',
                        value: 'admin',
                      },
                    ]}
                  />
                </Form.Input>

                <Button primary fluid size="large" onClick disabled={isFetching}>
                  ساخت حساب
                </Button>
              </Form>
            </Segment>
          </Grid.Column>
        </Grid.Row>
      </Grid >
    </Container>
  );
}


const mapStateToProps = (state) => ({
  isFetching: state.account.isFetching,
  isRegistered: state.account.isRegistered,
  isLoggedIn: state.account.token,
  wasRegistrationFailed: state.account.wasRegistrationFailed,
})

export default connect(mapStateToProps, {
  createAccount,
})(CreateAccount)